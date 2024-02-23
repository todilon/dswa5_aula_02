from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)
@app.route('/')
def hello_world():
    texto = """
            <h1>Avaliação contínua: Aula 030</h1>
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/aluno/Thiago Odilon Mariano Da Silva/PT3019969/IFSP">Identificação</a></li>
                <li><a href="/contextorequisicao">Contexto da requisição</a></li>
            </ul>
        """
    return texto

@app.route('/aluno/<nome>/<prontuario>/<inst>')
def aluno(nome, prontuario, inst):
    texto = """
            <h1>Avaliação contínua: Aula 030</h1>
            <h2>Aluno: """+ '{}'.format(nome) +"""</h2>
            <h2>Prontuário: """+ '{}'.format(prontuario) +"""</h2>
            <h2>Instituição: """+ '{}'.format(inst) +"""</h2>
            <p><a href="/">Voltar</a></p>
        """
    return texto

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent');
    texto = """
            <h1>Avaliação contínua: Aula 030</h1>
            <h2>Seu navegador é: """ + '{}'.format(user_agent) + """</h2>
            <h2>O IP do cumputador remoto é: """+ request.remote_addr + """</h2>
            <h2>O host da aplicação é: """ + request.host + """</h2>
            <p><a href="/">Voltar</a></p>
        """
    return texto