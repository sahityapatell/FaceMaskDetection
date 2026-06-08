// script.js — Face Mask Detection
// Plain simple JavaScript. No frameworks. Handles previews and webcam streaming.

// ── Tab switching ────────────────────────────────────────────────────────────
var tabBtns   = document.querySelectorAll('.tab-btn');
var tabPanels = document.querySelectorAll('.tab-panel');

for (var i = 0; i < tabBtns.length; i++) {
  tabBtns[i].addEventListener('click', function() {
    var target = this.dataset.tab;

    for (var j = 0; j < tabBtns.length; j++)   tabBtns[j].classList.remove('active');
    for (var j = 0; j < tabPanels.length; j++) tabPanels[j].classList.remove('active');

    this.classList.add('active');
    document.getElementById('tab-' + target).classList.add('active');
  });
}

// ── Show / hide helpers ──────────────────────────────────────────────────────
function show(id) { 
  var el = document.getElementById(id);
  if (el) el.style.display = 'block'; 
}
function hide(id) { 
  var el = document.getElementById(id);
  if (el) el.style.display = 'none'; 
}
function showFlex(id) { 
  var el = document.getElementById(id);
  if (el) el.style.display = 'flex'; 
}

// ─────────────────────────────────────────────────────────────────────────────
//  IMAGE DETECTION PREVIEW
// ─────────────────────────────────────────────────────────────────────────────
var imgInput = document.getElementById('img-input');
if (imgInput) {
  imgInput.addEventListener('change', function() {
    if (this.files[0]) {
      loadImagePreview(this.files[0]);
    }
  });
}

var imgDropZone = document.getElementById('img-drop-zone');
if (imgDropZone) {
  imgDropZone.addEventListener('click', function() {
    imgInput.click();
  });
  imgDropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    this.classList.add('drag-over');
  });
  imgDropZone.addEventListener('dragleave', function() {
    this.classList.remove('drag-over');
  });
  imgDropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    this.classList.remove('drag-over');
    if (e.dataTransfer.files[0]) {
      loadImagePreview(e.dataTransfer.files[0]);
    }
  });
}

function loadImagePreview(file) {
  var imgPreview = document.getElementById('img-preview');
  if (imgPreview) {
    imgPreview.src = URL.createObjectURL(file);
    hide('img-drop-zone');
    show('img-preview-area');
    hide('img-result');
  }
}

var imgClearBtn = document.getElementById('img-clear-btn');
if (imgClearBtn) {
  imgClearBtn.addEventListener('click', function() {
    if (imgInput) imgInput.value = '';
    show('img-drop-zone');
    hide('img-preview-area');
    hide('img-result');
  });
}

var imgForm = document.getElementById('image-form');
if (imgForm) {
  imgForm.addEventListener('submit', function() {
    hide('img-preview-area');
    showFlex('img-loader');
  });
}

// ─────────────────────────────────────────────────────────────────────────────
//  VIDEO DETECTION PREVIEW
// ─────────────────────────────────────────────────────────────────────────────
var vidInput = document.getElementById('vid-input');
if (vidInput) {
  vidInput.addEventListener('change', function() {
    if (this.files[0]) {
      loadVideoPreview(this.files[0]);
    }
  });
}

var vidDropZone = document.getElementById('vid-drop-zone');
if (vidDropZone) {
  vidDropZone.addEventListener('click', function() {
    vidInput.click();
  });
  vidDropZone.addEventListener('dragover', function(e) {
    e.preventDefault();
    this.classList.add('drag-over');
  });
  vidDropZone.addEventListener('dragleave', function() {
    this.classList.remove('drag-over');
  });
  vidDropZone.addEventListener('drop', function(e) {
    e.preventDefault();
    this.classList.remove('drag-over');
    if (e.dataTransfer.files[0]) {
      loadVideoPreview(e.dataTransfer.files[0]);
    }
  });
}

function loadVideoPreview(file) {
  var vidPreview = document.getElementById('vid-preview');
  if (vidPreview) {
    vidPreview.src = URL.createObjectURL(file);
    hide('vid-drop-zone');
    show('vid-preview-area');
    hide('vid-result');
  }
}

var vidClearBtn = document.getElementById('vid-clear-btn');
if (vidClearBtn) {
  vidClearBtn.addEventListener('click', function() {
    if (vidInput) vidInput.value = '';
    show('vid-drop-zone');
    hide('vid-preview-area');
    hide('vid-result');
  });
}

var vidForm = document.getElementById('video-form');
if (vidForm) {
  vidForm.addEventListener('submit', function() {
    hide('vid-preview-area');
    showFlex('vid-loader');
  });
}

// ─────────────────────────────────────────────────────────────────────────────
//  LIVE WEBCAM
// ─────────────────────────────────────────────────────────────────────────────
var webcamStartBtn = document.getElementById('webcam-start-btn');
if (webcamStartBtn) {
  webcamStartBtn.addEventListener('click', function() {
    var streamImg = document.getElementById('webcam-stream');
    if (streamImg) {
      streamImg.src = '/video_feed';
      hide('webcam-idle');
      show('webcam-live');
    }
  });
}

var webcamStopBtn = document.getElementById('webcam-stop-btn');
if (webcamStopBtn) {
  webcamStopBtn.addEventListener('click', function() {
    var streamImg = document.getElementById('webcam-stream');
    if (streamImg) {
      streamImg.src = '';
      hide('webcam-live');
      show('webcam-idle');
    }
  });
}
