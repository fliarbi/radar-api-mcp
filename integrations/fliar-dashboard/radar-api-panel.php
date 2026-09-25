<?php
// Accept only same-origin absolute paths; never hand a dashboard session to an external site.
$radar_developer_path = $site_config['radar_developer_path'] ?? '';
if (!is_string($radar_developer_path) ||
    !preg_match('~^/(?:[A-Za-z0-9_-]+/)*developer$~D', $radar_developer_path)) {
    $radar_developer_path = '';
}
?>
<section id="section-radarapi" class="dashboard-section hidden px-8 py-8">
    <div class="section-title">Radar API &amp; MCP</div>
    <p class="section-sub">Connect company, financial, funding, people and app data to your own application, Claude Code or Codex.</p>
    <div class="bg-white border border-[#d0c6ab]/20 rounded-xl p-6" style="max-width:880px;line-height:1.65">
        <h2 class="text-xl font-bold mb-3">Create your Radar API key</h2>
        <ol class="list-decimal pl-5 space-y-2 mb-5">
            <li>Sign in to your verified Fliar account.</li>
            <li>Open the developer console and choose <strong>Connect Radar session</strong>.</li>
            <li>Enter an application name, choose data access and set an expiry.</li>
            <li>Choose <strong>Create API key</strong> and copy it once into your application's secret store.</li>
        </ol>
        <?php if ($radar_developer_path !== ''): ?>
        <a id="radar-api-console-link" href="<?= htmlspecialchars($radar_developer_path, ENT_QUOTES, 'UTF-8') ?>" class="inline-flex items-center gap-2 rounded-lg bg-[#705d00] text-white px-5 py-3 font-bold">Create or manage API keys</a>
        <p class="mt-3 text-sm">The console shows your API base URL, MCP URL, key scopes, expiry and usage. Revoke a key there when you no longer need it.</p>
        <?php else: ?>
        <p id="radar-api-unavailable" role="status" class="border-l-4 border-[#705d00] pl-4 py-2"><strong>Private API access is not enabled on this dashboard yet.</strong><br>Ask your Fliar account administrator to enable the Radar developer connection. This page cannot create a working key until that connection is configured.</p>
        <?php endif; ?>
        <hr class="my-6 border-[#d0c6ab]/30">
        <h3 class="font-bold">Which key do I need?</h3>
        <p class="mt-2"><code>rdr_…</code> is a Radar API key for this REST/MCP gateway. The <strong>Prism News API</strong> section manages a separate News credential. It does not issue a Radar key.</p>
        <p class="mt-3">Your key follows your linked Radar plan and API credit limits. Contact retrieval needs an explicit contacts scope and entitled account. Pay-per-use checkout appears only when the operator has activated pricing.</p>
        <details class="mt-5"><summary class="font-bold cursor-pointer">My key or Radar session stopped working</summary><p class="mt-2">Sign in to Fliar again, open the developer console and reconnect your Radar session. If the API key itself is expired or revoked, create a replacement and update your application. Do not paste a key or session token into a support message.</p></details>
    </div>
</section>
