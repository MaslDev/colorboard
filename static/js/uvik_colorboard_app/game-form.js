$.validator.addMethod("lettersOnly", function (value, element) {
    return this.optional(element) || /^[A-Za-z]+$/i.test(value);
}, "Letters only please");


$(document).ready(function () {
    $("#game-form").validate({
        rules: {
            number_of_players: {
                required: true,
                min: 1,
                max: 4,
            },
            number_of_squares: {
                required: true,
                min: 1,
                max: 79,
            },
            number_of_cards: {
                required: true,
                min: 1,
                max: 200,
            },
            characters_on_board: {
                required: true,
                lettersOnly: true,
                maxlength: 79,
            },
            cards_in_deck: {
                required: true,
                maxlength: 400,
            }
        },
        messages: {
            number_of_players: {
                required: "This field is required",
                min: "Min:1",
                max: "Max:4",
            },
            number_of_squares: {
                required: "This field is required",
                min: "Min:1",
                max: "Max:79",
            },
            number_of_cards: {
                required: "This field is required",
                min: "Min:1",
                max: "Max:200",
            },
            characters_on_board: {
                required: "This field is required",
                maxlength: "Max: 79",
            },
            cards_in_deck: {
                required: "This field is required",
                maxlength: "Max: 200 characters(as​ ​a​ ​comma​ ​separated​ ​string)",
            }
        },
        submitHandler: function () {
            let $thisForm = $('#game-form');
            let $thisUrl = $thisForm.attr('data-url') || window.location.href;
            let $formData = $thisForm.serialize();
            $.ajax({
                method: 'POST',
                url: $thisUrl,
                data: $formData,
                success: function (response_data) {
                    alert(response_data.result)
                }
            });
        }

    });

});
