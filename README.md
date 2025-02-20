# Database Query Assistant 🤖

## Overview
Database Query Assistant is a powerful web application that allows users to query databases using natural language. Built with Python and Google's Gemini AI, it supports multiple database formats and provides intuitive responses to database queries.
--------------------------------------------------
## 🌟 Features

- **Natural Language Querying**: Ask questions about your database in plain English
- **Multiple Database Support**:
  - SQL databases (.sql files)
  - MongoDB collections (.json files)
  - CSV files
- **Interactive Chat Interface**: User-friendly chat interface for query interactions
- **Real-time Processing**: Instant database processing and query responses
- **Secure API Handling**: Secure management of Google API keys
- **Error Handling**: Robust error handling and user feedback
- **Responsive Design**: Clean and responsive UI built with Streamlit
-------------------------------------------------
## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
-------------------------------------------------
### Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/database-query-assistant.git
cd database-query-assistant
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
`--------------------------------------------------``

### 🔑 API Key Setup

1. Obtain a Google API key:
   - Visit the [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select an existing one
   - Enable the Gemini API
   - Create credentials (API key)

2. Store your API key securely (optional):
   - Create a `.env` file in the project root
   - Add your API key: `GOOGLE_API_KEY=your_api_key_here`
---------------------------------------------------
## 💻 Usage

1. Start the application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided URL (typically `http://localhost:8501`)

3. Enter your Google API key in the sidebar

4. Upload your database file:
   - Supported formats: .sql, .json, .csv
   - Wait for processing confirmation

5. Start querying:
   - Type your questions in natural language
   - View responses in the chat interface
---------------------------------------------------
### Example Queries

```plaintext
"What are the total sales for each month?"
"Show me the top 5 customers by revenue"
"What is the average transaction value?"
"List all orders from the last quarter"
```
-----------------------------------------------------
## 📁 Project Structure

```
database-query-assistant/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables (create this)
```
------------------------------------------------------
## 🛠️ Configuration

The application can be configured through the following environment variables:

- `GOOGLE_API_KEY`: Your Google API key
- `STREAMLIT_SERVER_PORT`: Custom port for Streamlit server
- `STREAMLIT_SERVER_ADDRESS`: Custom address for Streamlit server
------------------------------------------------------
## 🔒 Security Considerations

- Never commit your API keys to version control
- Use environment variables for sensitive information
- Regularly rotate your API keys
- Validate and sanitize all user inputs
-------------------------------------------------------
## 🐛 Troubleshooting

Common issues and solutions:
-------------------------------------------------------
1. **API Key Error**:
   - Verify your API key is correct
   - Ensure the Gemini API is enabled in your Google Cloud Console
-------------------------------------------------------
2. **File Upload Issues**:
   - Check file format compatibility
   - Ensure file is not corrupted
   - Verify file size is within limits
-------------------------------------------------------
3. **Processing Errors**:
   - Check database file format
   - Ensure proper file encoding (UTF-8)
   - Verify database schema is valid
------------------------------------------------------
## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
------------------------------------------------------
## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
-------------------------------------------------------
## 🙏 Acknowledgments

- Google Gemini AI for natural language processing
- Streamlit for the web interface
- The open-source community for various dependencies
-------------------------------------------------------
## 📞 Support

For support, please:
1. Check the troubleshooting section
2. Create an issue in the repository
3. Contact the maintainers
--------------------------------------------------------
## 🔄 Updates

Stay updated with the latest changes:
- Star and watch the repository
- Check the releases page
- Follow the maintainers

------------------------------------------------------
Made with ❤️ by Shivam Kumar
© 2024 Shivam Kumar. All rights reserved.