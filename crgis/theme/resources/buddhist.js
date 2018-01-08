// Buddhist.js


var vm = new Vue({
    el: '#query-filter',
    data: {
        message: 'Hello Vue!',
        result: []
    }
})

$(document).ready(function(){
    // 地區 展開/收合
    $('.oc-area').click(function(){
        $('div.area').slideToggle()
    })

    // 類別 展開/收合
    $('.oc-ctgr').click(function(){
        $('div.ctgr').slideToggle()
    })


    // 勾選縣市，其下各區全選 / 全不選
    $('input.area').change(function(){
        if(this.checked){
            $(this).siblings('div.area').find('input').prop('checked', true)
        }else{
            $(this).siblings('div.area').find('input').prop('checked', false)
        }
    })

    // 勾選類別 全選 / 全不選
    $('input.ctgr').change(function(){
        if(this.checked){
            $(this).siblings('div.ctgr').find('input').prop('checked', true)
        }else{
            $(this).siblings('div.ctgr').find('input').prop('checked', false)
        }
    })

    $('.all').change(function(){
        if($(this).val() == 'all-area'){
            if(this.checked){
                $('input.area').prop("checked", true);
            }else{
                $('input.area').prop("checked", false)
            }

        } else if($(this).val() == 'all-ctgr'){
            if(this.checked){
                $('input.ctgr').prop("checked", true);
            }else{
                $('input.ctgr').prop("checked", false)
            }
        }
    })
})


var marker = []
var getData = function(){
        // 地區絛件
        items = $('.criterion input.area:checked')
        area = []
        for(i=0; i<items.length; i++){
            area.push(items[i].value)
        }

        // 類別條件
        items = $('.criterion input.ctgr:checked')
        bgis_type = []
        for(i=0; i<items.length; i++){
            bgis_type.push(items[i].value)
        }

        data = {
           'area': area,
           'bgis_type': bgis_type
        }

//console.log(data)
        $.post(
            '/crgis/@@bdst_query',
            data=data
        ).done(function(returnData){
            jsonData = $.parseJSON(returnData) // OK, VUE.js
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
    $('.criterion input').change(function(){
        getData()
    })

})


