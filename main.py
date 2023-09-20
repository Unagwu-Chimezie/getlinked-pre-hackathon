from app import create_app
from dotenv import load_dotenv
import os
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
app = create_app(os.getenv('GETLINKED_CONFIG') or 'production')

@app.context_processor
def inject_sitewide_features():
    SITENAME = "GETLINKED"
    return dict(SITENAME=SITENAME,        
    )

if __name__ == "__main__" :
    app.run(ssl_context="adhoc")
