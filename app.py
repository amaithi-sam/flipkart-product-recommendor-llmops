from flask import render_template, Flask, request, Response 
from prometheus_client import Counter, generate_latest 
from dotenv import load_dotenv 
load_dotenv()

from flipkart.data_ingestion import DataIngestor
from flipkart.rag_chain import RAGChainBuilder 

REQUEST_COUNT = Counter("http_request_total", " Total Http Request")
INFERENCE_COUNT = Counter("RAG_Inference_total", " Total Inference request")



def create_app():

    app = Flask(__name__)

    vector_store = DataIngestor().ingest(load_existing=True)

    rag_chain = RAGChainBuilder(vector_store).build_chain()

    @app.route("/")
    def index():
        REQUEST_COUNT.inc()

        return render_template("index.html")
    


    @app.route("/get", methods=['POST'])
    def get_response():
        
        user_input = request.form["msg"]

        response = rag_chain.invoke({'input': user_input}, config={'configurable': {'session_id': "user-session"}})['answer']

        INFERENCE_COUNT.inc()

        return response 
    

    @app.route("/metrics")
    def metrics():
        return Response(generate_latest(), mimetype="text/plain")
    
    return app
    


if __name__ == "__main__":
    app = create_app()
    app.run(host = "0.0.0.0", port=5000, debug=False)