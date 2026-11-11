"use strict";
// Consent page for OAuth connector sign-in. It never sees a client secret or the PKCE verifier;
// it only approves, with the Companies Radar session this domain already holds, the parameters the server
// validated before rendering this page.
(function () {
  var cfg;
  try { cfg = JSON.parse(document.getElementById("oauth-config").textContent); }
  catch (e) { return; }
  var params = (cfg && cfg.params) || {};
  var errorEl = document.getElementById("error");

  function show(id, on) { var el = document.getElementById(id); if (el) el.hidden = !on; }
  function fail(msg) { if (errorEl) errorEl.textContent = msg; }

  var nameEl = document.getElementById("client-name");
  if (nameEl && cfg && cfg.client_name) nameEl.textContent = cfg.client_name;

  function session() {
    try { return localStorage.getItem("radar_auth_token") || ""; } catch (e) { return ""; }
  }

  // Build the client's redirect, preserving any query it already carries.
  function redirectWith(extra) {
    var uri = params.redirect_uri || "";
    var sep = uri.indexOf("?") >= 0 ? "&" : "?";
    var qs = Object.keys(extra).map(function (k) {
      return encodeURIComponent(k) + "=" + encodeURIComponent(extra[k]);
    }).join("&");
    return uri + sep + qs;
  }

  var token = session();
  if (!token) {
    show("signed-out", true);
    // The login page honours a same-origin ?next=, so signing in (or registering) returns here.
    var link = document.getElementById("login-link");
    if (link && location.origin === new URL(link.href).origin) {
      link.href = link.href + "?next=" + encodeURIComponent(location.href);
      link.removeAttribute("target");
    }
    // Signing in from another tab on this origin writes the session; pick it up without a manual reload.
    window.addEventListener("storage", function (e) {
      if (e.key === "radar_auth_token" && e.newValue) location.reload();
    });
    document.addEventListener("visibilitychange", function () {
      if (!document.hidden && session()) location.reload();
    });
    return;
  }
  show("signed-in", true);

  var allow = document.getElementById("allow");
  var deny = document.getElementById("deny");

  if (deny) {
    deny.addEventListener("click", function () {
      var state = params.state;
      location.href = redirectWith(state ? { error: "access_denied", state: state } : { error: "access_denied" });
    });
  }

  if (allow) {
    allow.addEventListener("click", function () {
      allow.disabled = true;
      fail("");
      var body = new URLSearchParams();
      ["client_id", "redirect_uri", "response_type", "code_challenge",
       "code_challenge_method", "scope", "state"].forEach(function (k) {
        if (params[k] !== undefined && params[k] !== null && params[k] !== "") body.append(k, params[k]);
      });
      fetch(location.pathname, {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded", "X-Auth-Token": token },
        body: body.toString()
      }).then(function (r) {
        return r.json().then(function (data) { return { status: r.status, data: data }; });
      }).then(function (res) {
        if (res.status === 200 && res.data && res.data.redirect) {
          location.href = res.data.redirect;
          return;
        }
        allow.disabled = false;
        var d = res.data || {};
        if (res.status === 401) fail((d.error_description || "Your session has expired.") + " Sign in to Companies Radar and try again.");
        else fail(d.error_description || "Authorization could not be completed. Please try again.");
      }).catch(function () {
        allow.disabled = false;
        fail("Network error. Please try again.");
      });
    });
  }
})();
