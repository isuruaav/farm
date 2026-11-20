'use strict';

(() => {
  function setupScrollReveal() {
    if (!('IntersectionObserver' in window)) return;
    const motionPreference = window.matchMedia?.('(prefers-reduced-motion: reduce)');
    if (motionPreference?.matches) return;

    const pending = new Set();
    let observer;

    function reveal(element) {
      element.classList.remove('is-pending');
      pending.delete(element);
      observer?.unobserve(element);
    }

    function revealAll() {
      pending.forEach(reveal);
      observer?.disconnect();
    }

    try {
      observer = new window.IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) reveal(entry.target);
        });
      }, { threshold: 0, rootMargin: '0px 0px -32px 0px' });

      const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
      document.querySelectorAll('#main-content > section').forEach(section => {
        // Keep sticky controls and section backgrounds stationary; animate the content.
        if (section.matches('.sticky, .catalog-filters, [data-reveal="off"]')) return;
        const content = [...section.children].find(child => child.matches('.site-container, [class*="max-w-"]')) || section.firstElementChild;
        if (!content || !content.getClientRects().length) return;
        content.classList.add('scroll-reveal');

        // Keep the first screen and restored scroll positions immediately readable.
        if (content.getBoundingClientRect().top < viewportHeight) return;
        content.classList.add('is-pending');
        pending.add(content);
        observer.observe(content);
      });

      // Keyboard navigation must never land on visually hidden content.
      document.addEventListener('focusin', event => {
        const content = event.target.closest?.('.scroll-reveal.is-pending');
        if (content) reveal(content);
      });
      motionPreference?.addEventListener?.('change', event => {
        if (event.matches) revealAll();
      });
      window.addEventListener('beforeprint', revealAll);
    } catch {
      // Leave the entire page readable if animation support fails during setup.
      revealAll();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', setupScrollReveal, { once: true });
  } else {
    setupScrollReveal();
  }
})();
