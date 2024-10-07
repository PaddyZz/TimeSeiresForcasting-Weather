from src.weatherTSF.components.single_step_models import compile_and_fit
from src.weatherTSF.components.data_windowing import WindowGenerator
import tensorflow as tf

def autoregressive_LSTM_Evaluate(feedback_model,train_df,val_df,test_df):
    multi_window = WindowGenerator(
    input_width=24, label_width=24, shift=24,
    train_df=train_df,
    val_df=val_df,
    test_df=test_df,
    label_columns=None)
    _ = compile_and_fit(feedback_model, multi_window)
    model_path = './src/weatherTSF/models/autoreg_LSTM.keras'
    feedback_model.save(model_path)

    multi_window.plot(feedback_model)