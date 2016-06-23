        ymaps.ready(init);
        var myMap,
            myPlacemark;

        function init(){
            myMap = new ymaps.Map("map", {
               center: [55.87513027, 38.7936151],
                zoom: 9
            });

            myPlacemark = new ymaps.Placemark([55.87, 38.79], {
                hintContent: 'Москва!',
                balloonContent: 'Столица России'
            });

            myMap.geoObjects.add(myPlacemark);
        }