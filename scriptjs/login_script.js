 document.getElementById("form-login").addEventListener("submit", async (event) => {
      event.preventDefault();

      const formData = {
        email: document.getElementById("email").value,
        senha: document.getElementById("senha").value
      };

      try {
        const response = await fetch("http://127.0.0.1:8000/usuarios/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(formData)
        });

        if (response.ok) {
          const data = await response.json();
          alert("✅ " + data.message);
          // redirecionar, se quiser:
          // window.location.href = "home.html";
            window.location.href = "/html/deubom.html";
        } else {
          const err = await response.json();
          alert("❌ " + err.detail);
        }
      } catch (error) {
        alert("⚠️ Erro de conexão com o servidor.");
      }
    });