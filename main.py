from src.data_ingestion import data_ingestion
from src.data_preprocessing import data_preprocessing

# Orchestron Layer design : Entry point modeling

def main() : # Function Definition

  # Step 1 : Data loading
  df = data_ingestion()

  # Step 2 : Data Preprocessing and cleaning
  X_train,X_test,y_train,y_test = data_preprocessing(df)
  print(X_train.shape,X_test.shape,y_train.shape,y_test.shape)
main()       # Function calling