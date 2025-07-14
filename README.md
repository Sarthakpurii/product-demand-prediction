# Product Demand Prediction System

A machine learning-powered application that predicts product sales/demand using historical data and economic indicators. Features an intuitive PyQt5 GUI for easy interaction and real-time predictions.

## 🚀 Features

- **Sales Prediction**: Predicts demand for various food products.
- **Interactive GUI**: User-friendly PyQt5 interface with multiple pages for data input.
- **Economic Factors**: Incorporates inflation and unemployment rates for more accurate predictions.
- **Special Events**: Accounts for special promotions/events at different store locations.
- **Multi-Product Support**: Handles predictions for various products.

## 🛠️ Tech Stack

- **Python 3.x**
- **Machine Learning**
- **GUI Framework**
- **Data Processing**
- **Data Visualization**
- **Model Serialization**
- **Executable Packaging**

## 📋 Prerequisites

- Python 3.11 or higher (may work for lower 3.x versions)
- pip package manager

### For Running Executable
- Windows OS (for .exe file)
- No Python installation required

## 🚀 Quick Start (Executable)

### Download Latest Release (v1.0.0)

1. Go to the [Releases](https://github.com/SarthakPurii/product-demand-prediction/releases/tag/v1.0.0) page
2. Download `main.exe` from the Assets section
3. Run the downloaded executable
4. The application will start with the GUI interface

**No installation or Python required!**
## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/Sarthakpurii/product-demand-prediction.git
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
- Windows:
  ```bash
  .\.venv\Scripts\activate
  ```
- macOS/Linux:
  ```bash
  source .venv/bin/activate
  ```

4. Install required packages:
```bash
pip install -r requirements.txt
```

## 🎯 Usage

1. Run the main application:
```bash
python main.py
```

2. Follow the GUI workflow:
   - **Product Selection**: Choose the product you want to predict sales for.
   - **Store Special Events**: Select which stores (S001, S002, S003) will have special promotions.
   - **Day Selection**: Pick the day of the week for prediction.
   - **Economic Indicators**: Input current inflation and unemployment rates.
   - **View Prediction**: Get the predicted sales amount.

## 📁 Project Structure

```
product-demand-prediction/
│
├── core/                           
│   ├── constants/                  
│   │   ├── limits.py              
│   │   └── mappings.py            
│   └── utils/                     
│       └── preprocessing.py       
│
├── data/                          
│   ├── artificial_sales.csv      
│   ├── train_global_processed.csv      
│   ├── train.csv                 
│   ├── test.csv                  
│   ├── train_cleaned_data.csv                  
│   └── test_cleaned_data.csv        
│
├── data_processing/              
│   ├── eda_global.ipynb
│   ├── test_data_processing.ipynb
│   └── data_preprocessing_global.ipynb
│
├── model_strategies/             
│   └── model1_predicting_combined_sales/
│       ├── model_training.ipynb  
│       ├── rf_model.pkl          
│       └── preprocessor.pkl      
│
├── pyqt_gui/                     
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   ├── product_selector_page.py
│   │   ├── special_selector_page.py
│   │   ├── day_selector_page.py
│   │   ├── inflation_inputter_page.py
│   │   ├── unemployment_inputter_page.py
│   │   └── prediction_page.py   
│   │
│   ├── uis/
│   └── ui_pys/
│       ├── __init__.py
│       ├── product_selector.py
│       ├── special_selector.py
│       ├── day_selector.py
│       ├── inflation_inputter.py
│       ├── unemployment_inputter.py
│       └── prediction.py   
│
├── main.py                       # Application entry point
├── main.spec                     # To build your own binary executable file(.exe)
├── .gitignore                
├── requirements.txt              # Python dependencies
└── README.md                     
```

## 🔍 Development Notes

- Model training is done through Jupyter notebooks for transparency
- Data preprocessing includes cleaning and feature engineering
- The application follows a page-based navigation pattern

---

**Note**: Make sure to update the trained model and preprocessor files when retraining with new data.
```
