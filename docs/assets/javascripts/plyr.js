document$.subscribe(function() {
  const elements = document.querySelectorAll('video');
  
  elements.forEach(element => {
    if (!element.plyr) {
      new Plyr(element, {
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
