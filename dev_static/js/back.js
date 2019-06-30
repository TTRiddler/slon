$(document).ready(function(){
    $('#CallBackModal form button').click(function(e) {  // Обратный звонок
        e.preventDefault();

        csrf_token = $('#CallBackModal form [name="csrfmiddlewaretoken"]').val();
        phone = $('#CallbackPhone').val();
        
		data = {
            "csrfmiddlewaretoken": csrf_token,
            phone: phone,
        }

		$.ajax({
			type: "POST",
			url: $('#CallBackModal form').attr('action'),
			data: data,
			success: function(data) {
                $('#CallBackModal form').removeClass('needs-validation');
                $('#CallBackModal form').addClass('was-validated');
                if(data.sended==1) {
                    $('#CallBackModal .form-successed').removeClass('d-none');
                    $('#CallBackModal .form-successed').addClass('d-flex');
                } else if(data.sended==0) {
                    $('#CallBackModal .alert-danger').removeClass('d-none');
                }
            }
		});
    });

    $('#BooknowForm button').click(function(e) {  // Запись на пробное занятие
        e.preventDefault();

        csrf_token = $('#BooknowForm [name="csrfmiddlewaretoken"]').val();
        recaptcha = $('#BooknowForm [name="g-recaptcha-response"]').val();
        parent_name = $('#ParentName').val();
        phone = $('#SignPhone').val();
        child_name = $('#ChildName').val();
        age = $('#SignAge').val();
        sex = $('#BooknowForm [name="customRadio"]:checked').val();
        text = $('#Expectation').val();
        
		data = {
            "csrfmiddlewaretoken": csrf_token,
            'g-recaptcha-response': recaptcha,
            parent_name: parent_name,
            phone: phone,
            child_name: child_name,
            age: age,
            sex: sex,
            text: text,
        }

		$.ajax({
			type: "POST",
			url: $('#BooknowForm').attr('action'),
			data: data,
			success: function(data) {
                $('#BooknowForm').removeClass('needs-validation');
                $('#BooknowForm').addClass('was-validated');
                if(data.sended==1) {
                    $('#BooknowForm').siblings('.form-successed').removeClass('d-none');
                    $('#BooknowForm').siblings('.form-successed').addClass('d-flex');
                } else if(data.sended==0) {
                    $('#BooknowForm').siblings('.alert1').removeClass('d-none');
                } else if(data.sended==2) {
                    $('#BooknowForm').siblings('.alert2').removeClass('d-none');
                }
            }
		});
    });

    $('#BooknowForm2 button').click(function(e) {  // Запись на пробное занятие
        e.preventDefault();

        csrf_token = $('#BooknowForm2 [name="csrfmiddlewaretoken"]').val();
        recaptcha = $('#BooknowForm2 [name="g-recaptcha-response"]').val();
        parent_name = $('#ParentName2').val();
        phone = $('#SignPhone2').val();
        child_name = $('#ChildName2').val();
        age = $('#SignAge2').val();
        sex = $('#BooknowForm2 [name="customRadio2"]:checked').val();
        text = $('#Expectation2').val();
        
		data = {
            "csrfmiddlewaretoken": csrf_token,
            'g-recaptcha-response': recaptcha,
            parent_name: parent_name,
            phone: phone,
            child_name: child_name,
            age: age,
            sex: sex,
            text: text,
        }

		$.ajax({
			type: "POST",
			url: $('#BooknowForm2').attr('action'),
			data: data,
			success: function(data) {
                $('#BooknowForm2').removeClass('needs-validation');
                $('#BooknowForm2').addClass('was-validated');
                if(data.sended==1) {
                    $('#BooknowForm2').siblings('.form-successed').removeClass('d-none');
                    $('#BooknowForm2').siblings('.form-successed').addClass('d-flex');
                } else if(data.sended==0) {
                    $('#BooknowForm2').siblings('.alert1').removeClass('d-none');
                } else if(data.sended==2) {
                    $('#BooknowForm2').siblings('.alert2').removeClass('d-none');
                }
            }
		});
    });

});
