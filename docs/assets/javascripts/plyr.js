document$.subscribe(function() {
  const elements = document.querySelectorAll('video');
  
  // Initialize the relative path.
  const scriptEl = document.currentScript ||
    document.querySelector('script[src*="assets/javascripts/plyr.js"]')
  const iconUrl = new URL('../stylesheets/elements/plyr.svg', scriptEl.src).href;

  elements.forEach(element => {
    if (!element.plyr) {
      new Plyr(element, {
        iconUrl: iconUrl,
        controls: ['play-large', 'play', 'progress', 'current-time', 'mute', 'volume', 'settings', 'fullscreen'],
        settings: ['quality', 'speed'],
        quality: {
          default: 1080,
          options: [1080, 540]
        }
      });
    }
  });
});
