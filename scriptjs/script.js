document.querySelector('form').addEventListener('submit', async (e) =>{
    e.preventDefault();

    const formData = {
        nome: document.getElementById('nome').value,
        senha: document.getElementById('senha').value,
        email: document.getElementById('email').value,
        data_nascimento: document.getElementById('data').value
    };

    try {
        // envia os dados para o backend FastAPI
        const response = await fetch("http://127.0.0.1:8000/usuarios/cadastro", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const result = await response.json();
            alert("Usuário cadastrado com sucesso!");
            console.log(result);
        } else {
            const error = await response.json();
            alert("Erro ao cadastrar usuário: " + JSON.stringify(error));
        }
    } catch (err) {
        alert("Erro de conexão com o servidor: " + err.message);
    }
})