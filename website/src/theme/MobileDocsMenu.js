/**
 * Mobile Docs Menu Button
 * Adds a floating button on doc pages to open the sidebar menu
 */

function addMobileDocsButton() {
  // Only run on mobile
  if (window.innerWidth > 996) return;
  
  // Check if we're on a docs page
  const isDocsPage = window.location.pathname.includes('/docs/');
  if (!isDocsPage) return;
  
  // Check if button already exists
  if (document.getElementById('mobile-docs-menu-btn')) return;
  
  // Create the floating button
  const button = document.createElement('button');
  button.id = 'mobile-docs-menu-btn';
  button.innerHTML = '📚';
  button.setAttribute('aria-label', 'Open documentation menu');
  button.setAttribute('title', 'Documentation Menu');
  
  // Style the button
  button.style.cssText = `
    position: fixed;
    bottom: 80px;
    left: 16px;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    border: none;
    font-size: 24px;
    cursor: pointer;
    z-index: 9000;
    box-shadow: 0 4px 20px rgba(99, 102, 241, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  `;
  
  // Hover effect
  button.addEventListener('mouseenter', () => {
    button.style.transform = 'scale(1.1)';
    button.style.boxShadow = '0 6px 30px rgba(99, 102, 241, 0.6)';
  });
  
  button.addEventListener('mouseleave', () => {
    button.style.transform = 'scale(1)';
    button.style.boxShadow = '0 4px 20px rgba(99, 102, 241, 0.5)';
  });
  
  // Click handler - open the hamburger menu
  button.addEventListener('click', () => {
    // Find and click the navbar toggle button
    const navbarToggle = document.querySelector('.navbar__toggle');
    if (navbarToggle) {
      navbarToggle.click();
    }
  });
  
  document.body.appendChild(button);
}

function removeMobileDocsButton() {
  const button = document.getElementById('mobile-docs-menu-btn');
  if (button) {
    button.remove();
  }
}

// Run on page load and navigation
if (typeof window !== 'undefined') {
  // Initial load
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', addMobileDocsButton);
  } else {
    addMobileDocsButton();
  }
  
  // Handle resize
  window.addEventListener('resize', () => {
    if (window.innerWidth > 996) {
      removeMobileDocsButton();
    } else {
      addMobileDocsButton();
    }
  });
  
  // Handle navigation (for SPA behavior)
  const originalPushState = history.pushState;
  history.pushState = function() {
    originalPushState.apply(this, arguments);
    setTimeout(addMobileDocsButton, 100);
  };
  
  window.addEventListener('popstate', () => {
    setTimeout(addMobileDocsButton, 100);
  });
}

export default function MobileDocsMenuModule() {
  // This is a client module - the code above runs on load
}
