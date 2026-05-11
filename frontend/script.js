const API_URL = 'http://localhost:8000';

// UI Elements
const splashScreen = document.getElementById('splashScreen');
const mainContent = document.getElementById('mainContent');
const topicInput = document.getElementById('topicInput');
const searchBtn = document.getElementById('searchBtn');
const btnText = document.querySelector('.btn-text');
const reportContent = document.getElementById('reportContent');
const exportOptions = document.getElementById('exportOptions');
const toast = document.getElementById('toast');

let currentReportId = '';

// Splash Screen Transition
window.addEventListener('DOMContentLoaded', () => {
    // 2.5s for loading bar animation to complete
    setTimeout(() => {
        splashScreen.style.opacity = '0';
        splashScreen.style.transform = 'scale(1.1)';
        setTimeout(() => {
            splashScreen.style.display = 'none';
            mainContent.style.opacity = '1';
            // Auto-focus the input for an intuitive user experience
            topicInput.focus();
        }, 1000);
    }, 2500);
});

// Search Logic
searchBtn.addEventListener('click', async () => {
    const topic = topicInput.value.trim();
    if (!topic) {
        showToast('SPECIFY RESEARCH PARAMETERS');
        return;
    }

    startLoading();

    try {
        const response = await fetch(`${API_URL}/research`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic })
        });

        const data = await response.json();

        if (response.ok) {
            renderReport(data.report);
            currentReportId = data.id;
            exportOptions.style.display = 'flex';
            exportOptions.style.gap = '10px';
            showToast('SYNTHESIS COMPLETE');
        } else {
            showToast('SYSTEM ERROR');
            reportContent.innerHTML = `<div class="empty-state"><h3>Synthesis Interrupted</h3><p>${data.detail}</p></div>`;
        }
    } catch (error) {
        console.error('Error:', error);
        showToast('SYSTEM CONNECTIVITY FAILURE');
    } finally {
        stopLoading();
    }
});

function renderReport(markdown) {
    // Using a simpler renderer or manual cleaning for the "no asterisks" requirement
    const cleanText = markdown.replace(/\*/g, '').replace(/"/g, '');
    reportContent.innerHTML = marked.parse(cleanText);
}

function startLoading() {
    searchBtn.disabled = true;
    btnText.textContent = 'SYNTHESIZING...';
    reportContent.innerHTML = `
        <div class="empty-state">
            <div class="neural-spinner"></div>
            <h3 style="color: #6366f1; letter-spacing: 4px; font-weight: 800;">SYNTHESIS IN PROGRESS</h3>
        </div>
    `;
    exportOptions.style.display = 'none';
}

function stopLoading() {
    searchBtn.disabled = false;
    btnText.textContent = 'START RESEARCH';
}

function showToast(message) {
    toast.textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

async function exportResult(format) {
    if (!currentReportId) return;
    const endpoint = `${API_URL}/export/${format}/${currentReportId}`;
    window.open(endpoint, '_blank');
}

topicInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') searchBtn.click();
});
