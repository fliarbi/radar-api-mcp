/* Account credentials stay in memory; no API key or session is written to storage. */
"use strict";
const $ = id => document.getElementById(id);
const consoleBase = new URL(document.currentScript.src).pathname.replace(/\/developer\/console\.js$/, "");
$("api-base-url").textContent = location.origin + consoleBase;
$("mcp-url").textContent = location.origin + consoleBase + "/mcp";
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
function price() {const enabled = Boolean(catalog?.checkout_enabled); $("buy-credits").disabled=!enabled;
  const amount = Number($("topup-credits").value) * (catalog?.credit_price_paise || 0) / 100;
  $("buy-credits").textContent=enabled ? `Buy credits for ₹${amount.toFixed(2)}` : "Checkout unavailable";
  $("checkout-note").textContent=enabled ? `₹${(catalog.credit_price_paise / 100).toFixed(2)} per credit. Credits appear after payment is confirmed.` : "Pay-per-use pricing has not been activated.";
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
bind("news-form", "submit", async () => {await api("/account/news-key", "PUT", {api_key:$("news-key").value});$("news-key").value="";status("News key linked. News availability also depends on the connected service.");});
bind("refresh", "click", async () => {await refresh();status("Usage updated.");});
$("topup-credits").addEventListener("input", price);
bind("topup-form", "submit", async () => {
  if (!catalog?.checkout_enabled) throw new Error("Checkout has not been activated.");
  if (!window.Razorpay) await new Promise((resolve,reject) => {const s=document.createElement("script");s.src="https://checkout.razorpay.com/v1/checkout.js";s.onload=resolve;s.onerror=()=>reject(new Error("Payment checkout could not load."));document.head.append(s);});
  const order=await api("/account/topups", "POST", {credits:Number($("topup-credits").value)});
  new window.Razorpay({key:order.key_id,order_id:order.order_id,amount:order.amount,currency:order.currency,
    name:"Fliar Radar",description:`${order.credits} API credits`,handler:async () => {status("Payment submitted. Credits will appear after confirmation. Refresh usage shortly.");try {await refresh();} catch(e){status(e.message,true);}}}).open();
});
