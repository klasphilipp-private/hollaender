// Hysteresis keeps the compact header stable while its height changes.
const siteHeader = document.querySelector('.site-header');
if (siteHeader) {
  const updateHeader = () => {
    if (window.scrollY > 120) siteHeader.classList.add('is-compact');
    else if (window.scrollY < 40) siteHeader.classList.remove('is-compact');
  };
  window.addEventListener('scroll', updateHeader, { passive: true });
  window.addEventListener('pageshow', updateHeader);
  updateHeader();
}
