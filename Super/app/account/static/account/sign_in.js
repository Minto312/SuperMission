const valid_data = function(){
    let username = $('#username').val()
    let password = $('#password').val()
    if(username == '' || password == ''){
        alert('入力されていない項目があります')
        return false
    }
}

const sendEmail = async function(){
    const email = document.getElementById('email').value
    if(email == ''){
        alert('メールアドレスを入力してください')
        return false
    }


    const [user_id, username] = await fetch(`query_email/${email}`)
        .then(response => {return response.json()})
        .then(data => {
            console.log('data  ' + data);
            return [data.user_id, data.username];
        })

    console.log(user_id)
    if(user_id == 'notFound'){
        alert('メールアドレスが登録されていません')
        return false
    }

    const templateVariables = {
        email: email,
        username: username,
        reset_url: `https://tks-r2021.f5.si:8080/account/sign_in/password_reset/${user_id}`,
    };
    console.log(templateVariables)
    emailjs.send(
        'service_super',
        'template_password_reset',
        templateVariables,
    ).then(
        (response) => {
            document.getElementById('success-message').style.display = 'block';
            console.log('SUCCESS!', response.status, response.text);
        },
        (error) => {
            document.getElementById('error-message').style.display = 'block';
            console.log('FAILED...', error);
        },
    )
}

const main = () => {
    document.getElementById('emailSubmit').addEventListener('click', () => {
        sendEmail()
    })
    

    document.getElementById('forgot-password').addEventListener('click', () => {
        document.getElementById('email-back').style.opacity = '1';
        document.getElementById('email-back').style.zIndex = '1';

        document.getElementById('cancel').addEventListener('click', () => {
            document.getElementById('email-back').style.opacity = '0';
            document.getElementById('email-back').style.zIndex = '-1';
        })

    })
}

window.onload = main