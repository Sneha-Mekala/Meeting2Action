// static/app.js - connects UI to /parse_transcript/
document.addEventListener("DOMContentLoaded", () => {
  const processBtn = document.getElementById("processBtn");
  const clearBtn = document.getElementById("clearBtn");
  const transcriptEl = document.getElementById("transcript");
  const meetingIdEl = document.getElementById("meetingId");
  const statusEl = document.getElementById("status");
  const reportArea = document.getElementById("reportArea");
  const placeholder = document.getElementById("placeholder");
  const rContent = document.getElementById("r-content");
  const rTitle = document.getElementById("r-title");
  const rSub = document.getElementById("r-sub");
  const downloadDocx = document.getElementById("downloadDocx");
  const downloadPdf = document.getElementById("downloadPdf");
  const downloadRtf = document.getElementById("downloadRtf");

  function showStatus(text, isError=false) {
    statusEl.textContent = text;
    statusEl.style.color = isError ? "#f87171" : "#9ca3af";
  }

  clearBtn.addEventListener("click", () => {
    transcriptEl.value = "";
    meetingIdEl.value = "";
    reportArea.classList.add("hidden");
    placeholder.classList.remove("hidden");
    showStatus("");
  });

  processBtn.addEventListener("click", async () => {
    const transcript = transcriptEl.value.trim();
    const meetingId = meetingIdEl.value.trim() || `meeting-${Date.now()}`;

    if (!transcript) {
      showStatus("Please paste a meeting transcript to process.", true);
      return;
    }

    showStatus("Processing meeting locally…");
    processBtn.disabled = true;
    clearBtn.disabled = true;
    processBtn.textContent = "PROCESSING…";

    try {
      const payload = { transcript, meeting_id: meetingId };
      const res = await fetch("/parse_transcript/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (!res.ok) {
        let msg = res.statusText;
        try {
          const err = await res.json();
          if (err.detail) msg = JSON.stringify(err.detail);
        } catch(e){}
        showStatus("Server error: " + msg, true);
        return;
      }

      const json = await res.json();

      // Switch panels
      placeholder.classList.add("hidden");
      reportArea.classList.remove("hidden");
      rTitle.textContent = `Meeting Summary – ${json.meeting_id}`;
      rSub.textContent = `Generated: ${new Date().toLocaleString()}`;

      // Try to fetch plain text report
      let textReport = "";
      if (json.reports && json.reports.report_text_path) {
        const txtName = json.reports.report_text_path.split(/[/\\]/).pop();
        const txtUrl = "/artifacts/reports/" + txtName;
        try {
          const r = await fetch(txtUrl);
          if (r.ok) textReport = await r.text();
        } catch(e) {
          textReport = "";
        }
      }

      if (!textReport) {
        textReport = buildFallback(json);
      }

      rContent.innerHTML = convertPlainToHtml(textReport);

      if (json.reports) {
        const dDocx = json.reports.report_docx_path && json.reports.report_docx_path.split(/[/\\]/).pop();
        const dPdf  = json.reports.report_pdf_path && json.reports.report_pdf_path.split(/[/\\]/).pop();
        const dRtf  = json.reports.report_rtf_path && json.reports.report_rtf_path.split(/[/\\]/).pop();

        if (dDocx) {
          downloadDocx.href = "/artifacts/reports/" + dDocx;
          downloadDocx.style.display = "inline-block";
        }
        if (dPdf) {
          downloadPdf.href = "/artifacts/reports/" + dPdf;
          downloadPdf.style.display = "inline-block";
        }
        if (dRtf) {
          downloadRtf.href = "/artifacts/reports/" + dRtf;
          downloadRtf.style.display = "inline-block";
        }
      }

      showStatus("Done. Report ready.");
    } catch (e) {
      console.error(e);
      showStatus("Unexpected error: " + e.message, true);
    } finally {
      processBtn.disabled = false;
      clearBtn.disabled = false;
      processBtn.textContent = "PROCESS MEETING";
    }
  });

  function buildFallback(json) {
    let parts = [];
    parts.push(`Meeting Summary – ${json.meeting_id}`);
    parts.push("");
    parts.push("Summary of Discussion:");
    parts.push(json.summary || "");
    parts.push("");
    parts.push("Extracted Action Items:");
    (json.action_items || json.actions_extracted || []).forEach((a, idx) => {
      parts.push(`${idx+1}. ${a.task}`);
      parts.push(`   Owner: ${a.owner || "Not assigned"}`);
      parts.push(`   Due: ${a.due || "Not specified"}`);
      parts.push("");
    });
    parts.push("Tasks Created:");
    (json.tasks || json.created_issues || []).forEach(t =>
      parts.push(`- ${t.id} – ${t.summary} (Owner: ${t.assignee || "No owner"}; Due: ${t.due || "Not specified"})`)
    );
    parts.push("");
    parts.push("Notifications Sent:");
    (json.notifications || []).forEach(n =>
      parts.push(`- Issue ${n.issue} -> status: ${n.email_status}`)
    );
    return parts.join("\n");
  }

  function convertPlainToHtml(plain) {
    const lines = plain.split("\n");
    let html = "";
    for (let ln of lines) {
      const t = ln.trim();
      if (!t) { html += "<br/>"; continue; }
      if (t.startsWith("Meeting Summary")) {
        html += `<h3>${escapeHtml(t)}</h3>`;
      } else if (t.startsWith("Date:")) {
        html += `<div class="meta-line"><em>${escapeHtml(t)}</em></div>`;
      } else if (t.endsWith(":") && t.indexOf(" ")>0) {
        html += `<h3>${escapeHtml(t.replace(":",""))}</h3>`;
      } else if (/^\d+\.\s/.test(t)) {
        html += `<div class="list-number">${escapeHtml(t)}</div>`;
      } else if (t.startsWith("- ")) {
        html += `<div class="bullet">${escapeHtml(t.slice(2))}</div>`;
      } else {
        html += `<div>${escapeHtml(t)}</div>`;
      }
    }
    return html;
  }

  function escapeHtml(s) {
    return s.replaceAll("&","&amp;").replaceAll("<","&lt;").replaceAll(">","&gt;");
  }
});