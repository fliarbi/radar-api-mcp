/* Account credentials stay in memory; no API key or session is written to storage. */
"use strict";
const $ = id => document.getElementById(id);
const consoleBase = new URL(document.currentScript.src).pathname.replace(/\/developer\/console\.js$/, "");
$("api-base-url").textContent = location.origin + consoleBase;
$("mcp-url").textContent = location.origin + consoleBase + "/mcp";
$("radar-base").textContent = location.origin + consoleBase;
function productUrl(id, url) {
  const cell = $(id); cell.replaceChildren();
  if (url) { const code = document.createElement("code"); code.textContent = url; cell.append(code); }
  else cell.textContent = "Opening soon; your key will work here when it does.";
}
let session = "", catalog = null;
function status(message, error = false) { $("status").textContent = message; $("status").classList.toggle("error", error); }
async function api(path, method = "GET", data) {
  const response = await fetch(consoleBase + path, {method, headers: {"X-Auth-Token": session, "Content-Type": "application/json"},
    body: data === undefined ? undefined : JSON.stringify(data), cache: "no-store", credentials: "omit"});
  const body = await response.json();
  if (!response.ok || !body.ok) throw new Error(body.error?.message || "The request could not be completed.");
  return body.data;
}
function bind(id, event, fn) {
  $(id).addEventListener(event, async e => { e.preventDefault();
    const button = e.currentTarget.matches("button") ? e.currentTarget : e.currentTarget.querySelector("button");
    if (button) button.disabled = true;
    try { await fn(); } catch (error) { status(error.message, true); }
    finally { if (button) button.disabled = false; if (id === "topup-form") price(); }
  });
}
function action(text, fn) { const b = document.createElement("button"); b.type = "button"; b.textContent = text;
  b.addEventListener("click", async () => { b.disabled = true; try { await fn(); } catch(e) {status(e.message, true);} finally {b.disabled=false;} }); return b; }
async function refresh() {
  const [keys, usage, following, plans] = await Promise.all([api("/account/keys"), api("/account/usage"), api("/account/following"), api("/account/plans")]);
  catalog = plans;
  productUrl("news-base", plans.products?.prism_news); productUrl("business-base", plans.products?.prism_business_news);
  $("key-list").replaceChildren();
  for (const key of keys) {
    const tr = document.createElement("tr"), expired = key.expires * 1000 <= Date.now();
    for (const value of [key.name, "…" + key.last4, new Date(key.expires * 1000).toLocaleDateString(), key.revoked ? "Revoked" : expired ? "Expired" : "Active"]) {
      const td = document.createElement("td"); td.textContent = value; tr.append(td);
    }
    const td = document.createElement("td");
    if (!key.revoked) td.append(action("Revoke", async () => {await api("/account/keys/" + encodeURIComponent(key.id), "DELETE"); await refresh(); status("API key revoked.");}));
    tr.append(td); $("key-list").append(tr);
  }
  if (!keys.length) {const tr = document.createElement("tr"), td = document.createElement("td"); td.colSpan=5;td.textContent="Create your first key to connect an application.";tr.append(td);$("key-list").append(tr);}
  $("plan-summary").textContent = `${usage.plan} plan · ${usage.month_utc} (UTC)`;
  $("included").textContent = `${usage.included_used_or_reserved.toLocaleString()} / ${usage.included_limit.toLocaleString()}`;
  $("wallet").textContent = usage.wallet_credits.toLocaleString(); $("spent").textContent = usage.prepaid_used_or_reserved.toLocaleString();
  $("spend-limit").value = usage.monthly_prepaid_limit;
  $("follow-limit").textContent = `${following.count} of ${following.limit} companies`;
  $("follow-list").replaceChildren();
  for (const company of following.companies) {const li = document.createElement("li"), label=document.createElement("span");label.textContent=company.domain;
    li.append(label, action("Unfollow", async () => {await api("/account/following/" + encodeURIComponent(company.domain), "DELETE");await refresh();status("Company removed from your API watchlist.");}));$("follow-list").append(li);}
  price();
}
const money = (minor, currency) => new Intl.NumberFormat(undefined, {style: "currency", currency, minimumFractionDigits: 2}).format(minor / 100);
function currencies() {
  const offered = catalog?.checkout_currencies || [], select = $("topup-currency");
  if (select.options.length === offered.length && [...select.options].every((o, i) => o.value === offered[i])) return;
  // Browsers report India as Asia/Kolkata or the older Asia/Calcutta.
  const india = /^Asia\/(Kolkata|Calcutta)$/.test(Intl.DateTimeFormat().resolvedOptions().timeZone) || /-IN$/i.test(navigator.language);
  const preferred = india ? "INR" : "USD";
  select.replaceChildren(...offered.map(c => new Option(c, c, false, c === preferred)));
  if (!offered.includes(preferred) && offered.length) select.value = offered[0];
}
function price() {const enabled = Boolean(catalog?.checkout_enabled); currencies();
  const currency = $("topup-currency").value, unit = catalog?.credit_prices_minor?.[currency] || 0, minimum = catalog?.min_topup_credits || 1;
  const input = $("topup-credits"), credits = Number(input.value);
  input.min = minimum; if (enabled && document.activeElement !== input && credits < minimum) input.value = minimum;
  $("buy-credits").disabled = !enabled || !unit || Number(input.value) < minimum;
  $("buy-credits").textContent = enabled && unit ? `Buy credits for ${money(Number(input.value) * unit, currency)}` : "Checkout unavailable";
  $("checkout-note").textContent = enabled && unit ? `${money(unit, currency)} per credit. Minimum ${minimum.toLocaleString()} credits (${money(catalog.min_topup_usd_cents, "USD")}). Credits appear after payment is confirmed.` : "Pay-per-use pricing has not been activated.";
}
async function connect(value) {session=value;try {await api("/account/session", "POST", {});await refresh();$("connect").hidden=true;$("workspace").hidden=false;$("session").value="";status("Radar account connected.");} catch(e) {session="";throw e;}}
bind("connect-form", "submit", () => connect($("session").value.trim()));
bind("connect-existing", "click", () => {const token=localStorage.getItem("radar_auth_token");if(!token) throw new Error("Sign in on this Radar domain first, or use the local development connection.");return connect(token);});
bind("disconnect", "click", () => {session="";catalog=null;$("workspace").hidden=true;$("connect").hidden=false;$("new-key").value="";$("key-reveal").hidden=true;$("key-list").replaceChildren();$("follow-list").replaceChildren();status("Disconnected from this console.");});
bind("key-form", "submit", async () => {const key=await api("/account/keys", "POST", {name:$("key-name").value,scopes:$("key-scope").value.split(","),expires_days:Number($("key-expiry").value)});$("new-key").value=key.api_key;$("key-reveal").hidden=false;await refresh();status("API key created. Copy it before leaving this page.");$("new-key").focus();});
bind("copy-key", "click", async () => {await navigator.clipboard.writeText($("new-key").value);status("API key copied.");});
bind("hide-key", "click", () => {$("new-key").value="";$("key-reveal").hidden=true;status("Key dismissed. You can revoke it and create a replacement if needed.");});
bind("spending-form", "submit", async () => {await api("/account/spending", "PUT", {monthly_credit_limit:Number($("spend-limit").value)});await refresh();status("Monthly prepaid spending limit saved.");});
bind("follow-form", "submit", async () => {await api("/account/following", "PUT", {domain:$("follow-domain").value});$("follow-domain").value="";await refresh();status("Company added to your API watchlist.");});
bind("refresh", "click", async () => {await refresh();status("Usage updated.");});
$("topup-credits").addEventListener("input", price);
$("topup-currency").addEventListener("change", price);
bind("topup-form", "submit", async () => {
  if (!catalog?.checkout_enabled) throw new Error("Checkout has not been activated.");
  if (!window.Razorpay) await new Promise((resolve,reject) => {const s=document.createElement("script");s.src="https://checkout.razorpay.com/v1/checkout.js";s.onload=resolve;s.onerror=()=>reject(new Error("Payment checkout could not load."));document.head.append(s);});
  const order=await api("/account/topups", "POST", {credits:Number($("topup-credits").value),currency:$("topup-currency").value});
  new window.Razorpay({key:order.key_id,order_id:order.order_id,amount:order.amount,currency:order.currency,
    name:"Fliar API credits",description:`${order.credits} credits for Radar and Prism News`,handler:async (resp) => {
      status("Payment received. Confirming…");
      try {await api("/account/topups/verify", "POST", resp); await refresh(); status(`${order.credits.toLocaleString()} credits added.`);}
      catch(e) {status(e.message + " Refresh usage shortly.", true); try {await refresh();} catch(_) {}}
    }}).open();
});
