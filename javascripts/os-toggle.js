/**
 * Global OS tab toggle for IntelliJ IDEA Setup Guide
 *
 * Renders a fixed-width two-button group "OS: [Windows] [macOS]" in the
 * site header, to the left of the dark/light mode toggle.
 *
 * Clicking a button switches all Windows/macOS tab sets on every page to
 * that OS. The choice persists in localStorage across page loads.
 *
 * Only affects tab sets whose labels are exactly "Windows" and "macOS".
 * Tab sets with other labels (e.g. Windows/macOS/Linux install tabs) are
 * untouched.
 *
 * Place at docs/javascripts/os-toggle.js and add to mkdocs.yml:
 *   extra_javascript:
 *     - javascripts/os-toggle.js
 */

(function () {
  var STORAGE_KEY = "preferred-os";
  var OS_WINDOWS  = "windows";
  var OS_MACOS    = "macos";

  function getSaved() {
    return localStorage.getItem(STORAGE_KEY) || OS_WINDOWS;
  }

  function save(os) {
    localStorage.setItem(STORAGE_KEY, os);
  }

  /**
   * Switch all OS-labelled tab sets to the given OS.
   * A tab set qualifies only if it has both "windows" and "macos" labels.
   */
  function applyOS(os) {
    var sets = document.querySelectorAll(".tabbed-set.tabbed-alternate");
    sets.forEach(function (set) {
      var labels = Array.from(set.querySelectorAll(".tabbed-labels label"));
      var texts  = labels.map(function (l) { return l.textContent.trim().toLowerCase(); });

      var winIdx = texts.indexOf("windows");
      var macIdx = texts.indexOf("macos");
      if (winIdx === -1 || macIdx === -1) return;

      var targetIdx = (os === OS_WINDOWS) ? winIdx : macIdx;
      var inputs = set.querySelectorAll('input[type="radio"]');
      if (inputs[targetIdx]) {
        inputs[targetIdx].click();
      }
    });
  }

  function updateButtons(winBtn, macBtn, currentOS) {
    if (currentOS === OS_WINDOWS) {
      winBtn.classList.add("os-active");
      macBtn.classList.remove("os-active");
    } else {
      macBtn.classList.add("os-active");
      winBtn.classList.remove("os-active");
    }
  }

  function injectToggle() {
    var option = document.querySelector(".md-header__option");
    if (!option) return;

    var currentOS = getSaved();

    var group = document.createElement("div");
    group.className = "os-toggle-group";

    var label = document.createElement("span");
    label.className = "os-toggle-label";
    label.textContent = "OS:";

    var winBtn = document.createElement("button");
    winBtn.className = "os-toggle-btn";
    winBtn.textContent = "Windows";
    winBtn.setAttribute("aria-label", "Show Windows shortcuts");
    winBtn.setAttribute("title", "Show Windows shortcuts");

    var macBtn = document.createElement("button");
    macBtn.className = "os-toggle-btn";
    macBtn.textContent = "macOS";
    macBtn.setAttribute("aria-label", "Show macOS shortcuts");
    macBtn.setAttribute("title", "Show macOS shortcuts");

    updateButtons(winBtn, macBtn, currentOS);

    winBtn.addEventListener("click", function () {
      save(OS_WINDOWS);
      updateButtons(winBtn, macBtn, OS_WINDOWS);
      applyOS(OS_WINDOWS);
    });

    macBtn.addEventListener("click", function () {
      save(OS_MACOS);
      updateButtons(winBtn, macBtn, OS_MACOS);
      applyOS(OS_MACOS);
    });

    group.appendChild(label);
    group.appendChild(winBtn);
    group.appendChild(macBtn);

    option.parentNode.insertBefore(group, option);
  }

  function applySaved() {
    var saved = getSaved();
    if (saved === OS_MACOS) {
      applyOS(OS_MACOS);
    }
  }

  function init() {
    injectToggle();
    setTimeout(applySaved, 120);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
