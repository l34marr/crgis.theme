// Wangye.js


var vm = new Vue({
    el: '#query-filter',
    data: {
        message: 'Hello Vue!',
        result: [],
        page: 0
    }
})

$(document).ready(function(){
    // 縣市 展開/收合
    $('.oc-all').click(function(){
        $('div.dist').slideToggle()
    })

    $('.oc-all-dist').click(function(){
        $(this).next('div.dist').slideToggle()
    })

    // 姓氏 展開/收合
    $('.oc-all-wy').click(function(){
        $('div.f_name').slideToggle()
    })

    $('.oc-all-f_name').click(function(){
        $(this).next('div.f_name').slideToggle()
    })


/*    $('input.county').click(function(){
        if(this.checked){
            $(this).siblings('div.dist').slideDown()
        }else{
            $(this).siblings('div.dist').slideUp()
        }
    })
    $('input#all-county').click(function(){
        if(this.checked){
            $('.county-div div.dist').slideDown()
        }else{
            $('.county-div div.dist').slideUp()
        }
    })
*/


    // 勾選縣市，其下各區全選 / 全不選
    $('input.county').change(function(){
        if(this.checked){
            $(this).siblings('div.dist').find('input').prop('checked', true)
        }else{
            $(this).siblings('div.dist').find('input').prop('checked', false)
        }
    })

    // 勾選鄉鎮市區，判斷是否取消全選
    $('input.dist').change(function(){
        if(! this.checked){
            county = $($(this)[0]).parents('div.county')[0]
            $(county).find('input.county').prop('checked', false)
        }
    })

    // 勾選王爺，其下各姓氏 全選 / 全不選
    $('input.family-name').change(function(){
        if(this.checked){
            $(this).siblings('div.f_name').find('input').prop('checked', true)
        }else{
            $(this).siblings('div.f_name').find('input').prop('checked', false)
        }
    })

    // 勾選王爺姓氏，判斷是否取消全選
    $('input.name').change(function(){
        if(! this.checked){
            family = $($(this)[0]).parents('div.family-name')[0]
            $(family).find('input.family-name').prop('checked', false)
        }
    })

    $('.all').change(function(){
        if($(this).val() == 'all-county'){
            if(this.checked){
                $('input.county').prop("checked", true);
                $('input.dist').prop("checked", true);
            }else{
                $('input.county').prop("checked", false);
                $('input.dist').prop("checked", false)
            }

        } else if($(this).val() == 'all-family-name'){
            if(this.checked){
                $('input.family-name').prop("checked", true);
                $('input.name').prop("checked", true);
            }else{
                $('input.family-name').prop("checked", false);
                $('input.name').prop("checked", false);
            }
        }
    })
})


var marker = []
var getData = function(){
        // 鄉鎮市區絛件
        items = $('.criterion input.dist:checked')
        area2 = []
        for(i=0; i<items.length; i++){
            area2.push(items[i].value)
        }

        // 王爺條件
        items = $('.criterion input.name:checked')
        wynm = []
        for(i=0; i<items.length; i++){
            wynm.push(items[i].value)
        }

        // 年份條件
        yearRange = $('#yearRange').val()
//        start = $('#start-year').val()
//        end = $('#end-year').val()

        // hostcmpn
        items = $('.criterion input.hostcmpn:checked')
        hostcmpn = []
        for(i=0; i<items.length; i++){
            hostcmpn.push(items[i].value)
        }

        // 登錄條件
        items = $('.criterion input.register:checked')
        subject = []
        for(i=0; i<items.length; i++){
            subject.push(items[i].value)
        }

        data = {
           'area2': area2,
           'wynm': wynm,
//           'end': end,
//           'start': start,
           'yearRange': yearRange,
           'hostcmpn': hostcmpn,
           'subject': subject
        }

        $.post(
            '/crgis/@@wgye_query',
            data=data
        ).done(function(returnData){
            jsonData = $.parseJSON(returnData) // OK, 接VUE.js
            if(jsonData == null){
                vm.result = []
            }else{
                vm.result = jsonData
            }

// leafmap
        if(marker.length > 0){
            for(i=0; i<marker.length; i++){
                map.removeLayer(marker[i])
            }
            marker = []
        }
        for(i=0; i<vm.result.length; i++){
            marker.push(L.marker(vm.result[i]['latlng'],
                        {'title': vm.result[i]['title'], 'riseOnHover': true}));
            marker[i].addTo(map);
            marker[i].bindPopup('寺廟名稱: <a target="_blank" href="' + vm.result[i]['url'] + '">' + vm.result[i]['title'] + '</a>')
        }

        }).fail(function(){
            alert('Fail')
        })





}

$(document).ready(function(){   
    $('.criterion input:not(.yearRange)').change(function(){
        getData()
    })

    // 年代拉條 值更新 post
    $('.range-slider').jRange({
        from: 1365,
        to: 2017,
        step: 1,
        scale: [1365, 1700, 2017],
        format: '%s',
        width: 600,
        showLabels: true,
        isRange : true,
        ondragend: function () {
            getData()
        }
    });

})

// Pagination
$(document).ready(function(){
    $('.page-nav').click(function(){
        if( $(this).hasClass('first-page') ){
            vm.page = 0
        }else if( $(this).hasClass('pre-page') ){
            vm.page --
        }else if( $(this).hasClass('next-page') ){
            vm.page ++
        }else{
            vm.page = parseInt(vm.result.length/20)
        }

        if( vm.page == 0 ){
            $('.page-nav').css('display', 'initial')
            $('.first-page').css('display', 'none')
            $('.pre-page').css('display', 'none')
        }else if ( vm.page == parseInt(vm.result.length/20) ){
            $('.page-nav').css('display', 'initial')
            $('.last-page').css('display', 'none')
            $('.next-page').css('display', 'none')
        }else{
            $('.page-nav').css('display', 'initial')
        }


    })
})
