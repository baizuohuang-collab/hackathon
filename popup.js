document.getElementById('shiftBtn').addEventListener('click', async () => {
  const mode = document.getElementById('mode').value;
  const rawNotes = document.getElementById('notes').value;
  const resultsDiv = document.getElementById('results');
  const taskList = document.getElementById('taskList');
  const quoteElem = document.getElementById('quote');

  resultsDiv.style.display = 'none';
  taskList.innerHTML = '<li>Analyzing context...</li>';
  resultsDiv.style.display = 'block';

  try {
    const response = await fetch('http://localhost:8000/api/shift-context', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mode, raw_notes: rawNotes })
    });

    const data = await response.json();

    // Render tasks
    taskList.innerHTML = '';
    data.top_3_tasks.forEach(task => {
      const li = document.createElement('li');
      li.textContent = task;
      taskList.appendChild(li);
    });

    quoteElem.textContent = `"${data.focus_quote}"`;

    // Open context URLs in new tabs automatically
    if (data.suggested_urls && data.suggested_urls.length > 0) {
      data.suggested_urls.forEach(url => {
        chrome.tabs.create({ url: url, active: false });
      });
    }

  } catch (err) {
    taskList.innerHTML = '<li style="color: #ef4444;">Error connecting to ContextShift API.</li>';
  }
});
