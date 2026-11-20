'use strict';

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-industry-explorer]').forEach(explorer => {
    const choices = [...explorer.querySelectorAll('[data-industry-choice]')];
    const panels = [...explorer.querySelectorAll('[data-industry-panel]')];
    const list = explorer.querySelector('.industry-choices');
    list.setAttribute('role', 'tablist');
    list.setAttribute('aria-orientation', 'vertical');
    function select(choice, focus = false) {
      choices.forEach(item => {
        const selected = item === choice;
        item.classList.toggle('is-selected', selected);
        item.setAttribute('aria-selected', String(selected));
        item.tabIndex = selected ? 0 : -1;
      });
      panels.forEach(panel => panel.hidden = panel.dataset.industryPanel !== choice.dataset.industryChoice);
      if (focus) choice.focus();
    }
    choices.forEach((choice, index) => {
      choice.setAttribute('role', 'tab');
      choice.setAttribute('aria-controls', 'sector-panel-' + choice.dataset.industryChoice);
      choice.addEventListener('click', event => { event.preventDefault(); select(choice); });
      choice.addEventListener('keydown', event => {
        let next;
        if (['ArrowDown','ArrowRight'].includes(event.key)) next = (index + 1) % choices.length;
        if (['ArrowUp','ArrowLeft'].includes(event.key)) next = (index - 1 + choices.length) % choices.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = choices.length - 1;
        if (next !== undefined) { event.preventDefault(); select(choices[next], true); }
        if (event.key === ' ') { event.preventDefault(); select(choice); }
      });
    });
    panels.forEach(panel => {
      panel.setAttribute('role', 'tabpanel');
      panel.setAttribute('aria-labelledby', 'sector-choice-' + panel.dataset.industryPanel);
      panel.tabIndex = 0;
    });
    if (choices.length) select(choices[0]);
  });

  const params = new URLSearchParams(location.search);
  document.querySelectorAll('[data-gallery-src]').forEach(button => button.addEventListener('click', () => {
    openGalleryModal(button.dataset.gallerySrc, button.dataset.galleryCaption);
  }));
  for (const name of ['industry','inquiry_type']) {
    const field = document.querySelector(`form[data-inquiry="contact"] select[name="${name}"]`);
    const value = params.get(name);
    if (field && value && [...field.options].some(option => option.value === value)) field.value = value;
  }
  document.querySelectorAll('[data-investment-project]').forEach(link => link.addEventListener('click', () => {
    const field = document.querySelector('form[data-inquiry="investment"] select[name="industry"]');
    if (field && [...field.options].some(option => option.value === link.dataset.investmentProject)) field.value = link.dataset.investmentProject;
  }));
});
