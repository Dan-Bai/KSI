# KSI framework (Reproduction)
[Original Paper](https://dl.acm.org/doi/10.1145/3308558.3313485)
[Original Repository](https://github.com/tiantiantu/KSI)

## Dataset

This framework contains already preprocessed Wikipedia knowledge. Additional MIMIC-III datasets (DIAGNOSES_ICD and NOTEEVENTS) are downloaded from PhysioNet.

## Dependencies

- python 3.7
- stop-words 2018.7.23
- torch 1.11.0
- numpy 1.22.3
- sklearn 0.0 
- Local file NOTEEVENTS.csv
- Local file DIAGNOSES_ICD.csv

## Setup
_This setup assumes running on AWS Deep Learning Base AMI (Ubuntu)_

- sudo apt-get update
- sudo apt-get python3.7
- sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
- sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
- python3 -m pip install pip
- python3 -m pip install --upgrade pip
- pip3 install stop_words torch numpy sklearn
- gzip -dk DIAGNOSES_ICD.csv.gz
- gzip -dk NOTEEVENTS.csv.gz

## Running

Run the following commands in order to preprocess MIMIC-III dataset and KSI framework.

```console
python preprocessing1.py
python preprocessing2.py
python preprocessing3.py
```

The following commands can then be ran for their respective models. The program will train and validate before outputing performance metrics for both baseline model and KSI integration.

```console
python KSI_LSTM.py
python KSI_LSTMatt.py
python KSI_CNN.py
python KSI_CAML.py
```
## Output

The following performance metrics are outputed

- Macro AUC
- Micro AUC
- Macro F1
- Micro F1
- Top-10 Recall
- Test Loss

## Results
_This model was trained and validated on a subset of 10,000 records_

|            | Macro AUC | Micro AUC | Macro F1 | Micro F1 | Test Loss | Top10 Recall |
| ---------- | --------- | --------- | -------- | -------- | --------- | ------------ |
| RNN        | 0.7605    | 0.938     | 0.0792   | 0.4974   | 0.0497    | 0.6423       |
| KSI+RNN    | 0.8139    | 0.9502    | 0.1614   | 0.5417   | 0.0477    | 0.7069       |
|            |           |           |          |          |           |              |
| RNNatt     | 0.7772    | 0.9446    | 0.1439   | 0.5473   | 0.0502    | 0.6798       |
| KSI+RNNatt | 0.8396    | 0.9572    | 0.2003   | 0.5847   | 0.045     | 0.7236       |
|            |           |           |          |          |           |              |
| CNN        | 0.7575    | 0.9267    | 0.1307   | 0.5407   | 0.0558    | 0.6549       |
| KSI+CNN    | 0.8055    | 0.9456    | 0.1956   | 0.5742   | 0.0532    | 0.7067       |
|            |           |           |          |          |           |              |
| CAML       | 0.7773    | 0.9445    | 0.1586   | 0.5793   | 0.0514    | 0.6985       |
| KSI+CAML   | 0.8339    | 0.9548    | 0.1929   | 0.5959   | 0.0491    | 0.7323       |