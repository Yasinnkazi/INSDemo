/* ============================================================
   SQL INJECTION DEMO - MAIN JAVASCRIPT
   Form validation, flash messages, copy-to-clipboard
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

    autoDismissFlashMessages();
    setupPayloadCopy();
    setupFormValidation();

});

/* -----------------------------------------------------------
   Auto-dismiss flash messages after 4 seconds
   ----------------------------------------------------------- */
function autoDismissFlashMessages() {
    const messages = document.querySelectorAll('.flash-message');
    messages.forEach(function (msg) {
        setTimeout(function () {
            fadeOut(msg);
        }, 4000);
    });
}

/* -----------------------------------------------------------
   Fade out an element and remove it
   ----------------------------------------------------------- */
function fadeOut(element) {
    var opacity = 1;
    var timer = setInterval(function () {
        if (opacity <= 0.1) {
            clearInterval(timer);
            if (element.parentNode) {
                element.remove();
            }
        }
        element.style.opacity = opacity;
        opacity -= 0.1;
    }, 30);
}

/* -----------------------------------------------------------
   Close button handler for flash messages
   ----------------------------------------------------------- */
document.addEventListener('click', function (e) {
    if (e.target.classList.contains('close-btn')) {
        var message = e.target.closest('.flash-message');
        if (message) {
            message.remove();
        }
    }
});

/* -----------------------------------------------------------
   Copy SQL Injection payload to clipboard
   ----------------------------------------------------------- */
function copyPayload(element) {
    var codeElement = element.querySelector('code');
    if (!codeElement) return;

    var payload = codeElement.textContent.trim();

    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(payload).then(function () {
            showCopiedFeedback(element);
        }).catch(function () {
            fallbackCopy(payload, element);
        });
    } else {
        fallbackCopy(payload, element);
    }
}

/* -----------------------------------------------------------
   Fallback copy method using textarea
   ----------------------------------------------------------- */
function fallbackCopy(text, element) {
    var textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    try {
        document.execCommand('copy');
        showCopiedFeedback(element);
    } catch (e) {
        /* Copy failed silently */
    }
    document.body.removeChild(textarea);
}

/* -----------------------------------------------------------
   Show "Copied!" feedback on the payload item
   ----------------------------------------------------------- */
function showCopiedFeedback(element) {
    var originalText = element.innerHTML;
    var feedback = document.createElement('span');
    feedback.textContent = 'Copied!';
    feedback.style.cssText =
        'margin-left:8px;color:#22c55e;font-weight:700;font-size:0.8rem;';

    var existing = element.querySelector('.copy-feedback');
    if (existing) existing.remove();

    feedback.className = 'copy-feedback';
    element.appendChild(feedback);

    setTimeout(function () {
        var fb = element.querySelector('.copy-feedback');
        if (fb) fb.remove();
    }, 1500);
}

/* -----------------------------------------------------------
   Setup payload copy from onclick attributes
   ----------------------------------------------------------- */
function setupPayloadCopy() {
    document.querySelectorAll('.payload-item[onclick]').forEach(function (item) {
        var originalClick = item.getAttribute('onclick');
        if (originalClick && originalClick.includes('copyPayload')) {
            item.addEventListener('click', function (e) {
                copyPayload(this);
            });
            item.removeAttribute('onclick');
        }
    });
}

/* -----------------------------------------------------------
   Client-side form validation
   ----------------------------------------------------------- */
function setupFormValidation() {
    var forms = document.querySelectorAll('.login-form');
    forms.forEach(function (form) {
        form.addEventListener('submit', function (e) {
            var username = form.querySelector('#username');
            var password = form.querySelector('#password');
            var valid = true;

            if (username) {
                username.style.borderColor = '';
                if (!username.value.trim()) {
                    username.style.borderColor = '#dc2626';
                    valid = false;
                }
            }

            if (password) {
                password.style.borderColor = '';
                if (!password.value.trim()) {
                    password.style.borderColor = '#dc2626';
                    valid = false;
                }
            }

            if (!valid) {
                e.preventDefault();
                showValidationError(form, 'Please fill in all fields');
            }
        });
    });
}

/* -----------------------------------------------------------
   Show a temporary validation error message
   ----------------------------------------------------------- */
function showValidationError(form, message) {
    var existing = form.querySelector('.validation-error');
    if (existing) existing.remove();

    var error = document.createElement('div');
    error.className = 'validation-error';
    error.textContent = message;
    error.style.cssText =
        'color:#fca5a5;font-size:0.85rem;padding:8px 12px;' +
        'background:rgba(220,38,38,0.1);border-radius:6px;' +
        'text-align:center;';

    form.insertBefore(error, form.firstChild);

    setTimeout(function () {
        if (error.parentNode) error.remove();
    }, 3000);
}

/* -----------------------------------------------------------
   Clear input borders on focus
   ----------------------------------------------------------- */
document.addEventListener('focusin', function (e) {
    if (e.target.tagName === 'INPUT') {
        e.target.style.borderColor = '';
    }
});
