function slider() {
    $('.slider').slick({
        arrows:true,
        adaptiveHeight: true,
        slidesToShow: 3,
        speed:1250,
        autoplay:true,
        autoplaySpeed: 2000,
        draggable:false,
        swipe:false,
        centerMode: true,
        variableWidth: true,
        responsive: [{
            breakpoints: 768,
            settings: {
                slidesToShow: 2
            }
        },{
            breakpoints: 480,
            settings: {
                slidesToShow: 1
            }
        }]
    });
}

function reg_form() {
    $('#form-reg').submit(function (e) {
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: (data) => {
                if ('errors' in data) {
                    $('#form-reg' + 'input').each((index, el) => {
                        $(el).removeClass('is-invalid').addClass('is-valid')
                    })
                }

                $('#form-reg .invalid-feedback').each((index, el) => {
                    $(el).remove()
                })

                for (let key in data['errors']) {
                    $('#form-reg').find('input[name="' + key + '"]').removeClass('is-valid').addClass('is-invalid')

                    $('#form-reg').find('input[name="' + key + '"]').after(() => {
                        let result = ''
                        for(let k in data['errors'][key]) {
                            result += data['errors'][key][k] + '<br>'
                        }
                        return '<div class="invalid-feedback">' + data['errors'][key] + '</div>'
                    })
                }
                if ('success' in data) {
                    window.location.href = '/'
                }
            }
        })
    })
}

function log_form() {
    $('#form-login').submit(function (e){
        e.preventDefault()
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: 'json',
            success: function () {
                window.location.reload()
            },
            error: function (response) {
                if (response.status === 404){
                    $('.alert-danger').text(response.responseJSON.error).removeClass('d-none')
                }
            }
        })
    })
}