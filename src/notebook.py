## 
import os
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib tk
##

## {{{ constants
SEED = 3
## }}}

## {{{ loading dataset
dirname = os.path.join(os.path.abspath(".."), "data", "raw")
train = pd.read_excel(os.path.join(dirname, "train.xlsx"))
test = pd.read_csv(os.path.join(dirname, "test.csv"))
## }}}

## {{{ missing values, dtypes, shapes and nunique
print("TRAIN DATASET:")
print(train.info())
print("\nTEST DATASET:")
print(test.info())
# TRAIN DATASET:
# <class 'pandas.DataFrame'>
# RangeIndex: 14248 entries, 0 to 14247
# Data columns (total 10 columns):
#  #   Column                      Non-Null Count  Dtype
# ---  ------                      --------------  -----
#  0   __source_file               7950 non-null   str
#  1   cve_ids                     14248 non-null  str
#  2   cwe_ids                     14248 non-null  str
#  3   file_path                   14248 non-null  str
#  4   label                       14248 non-null  int64
#  5   patched_function_source     14147 non-null  str
#  6   predicted_cwe_ids           8830 non-null   str
#  7   repo                        14248 non-null  str
#  8   sha                         14248 non-null  str
#  9   vulnerable_function_source  14193 non-null  str
# dtypes: int64(1), str(9)
# memory usage: 1.1 MB
# None
# 
# TEST DATASET:
# <class 'pandas.DataFrame'>
# RangeIndex: 3563 entries, 0 to 3562
# Data columns (total 10 columns):
#  #   Column                   Non-Null Count  Dtype
# ---  ------                   --------------  -----
#  0   __source_file            1962 non-null   str
#  1   cve_ids                  3563 non-null   str
#  2   cwe_ids                  3563 non-null   str
#  3   file_path                3563 non-null   str
#  4   class                    3563 non-null   int64
#  5   patched_function_source  3545 non-null   str
#  6   predicted_cwe_ids        2204 non-null   str
#  7   repo                     3563 non-null   str
#  8   sha                      3563 non-null   str
#  9   function_code            3563 non-null   str
# dtypes: int64(1), str(9)
# memory usage: 278.5 KB
# None
## }}}

## {{{ viewing dataset samples
print("\nTRAINING SAMPLES:")
print(train.sample(10, random_state=SEED))
# TRAINING SAMPLES:
#                             __source_file  cve_ids  ...                                       sha                         vulnerable_function_source
# 13098  functions_for_airflow_with_cwe.csv  UNKNOWN  ...  af0c83e9bf84e3a0dff782e3a95a9b610d23643d  def _reset_signals():\n    # Uninstall the ric...
# 1945    functions_for_django_with_cwe.csv  UNKNOWN  ...  3b2993ed04f200a89c2d49590131c97c8974e9ac  def get_year(self):\n        """\n        Retu...
# 4176   functions_for_ansible_with_cwe.csv  UNKNOWN  ...  e6190524248ef2747c70e5c04377e78eb63e4d76  def __init__(self, *args, **kwargs):\n        ...
# 4452                                  NaN  UNKNOWN  ...  279f1fae1e8ef08eaff7a3505029fc2cc0508302  def test_async_execute_logging_should_execute_...
# 2005    functions_for_mlflow_with_cwe.csv  UNKNOWN  ...  fc19cde859e92b6e5dcc882a2742e4648e86b4ac  def collect_metrics(self):\n        # Get GPU ...
# 11237                                 NaN  UNKNOWN  ...  64968b7d645e8696492c6455be4692400567f1e3  def initdb():\n    from airflow import models\...
# 9191      functions_for_salt_with_cwe.csv  UNKNOWN  ...  af2a3028d3d18437b5b9f17a96c1f3ebafb7d1db  def install(name=None,\n            refresh=Fa...
# 4179    functions_for_mlflow_with_cwe.csv  UNKNOWN  ...  1ecbd4ac8b16716d2ba08517cec62245d5d20374  def _get_user_defined_estimator(self, X_train,...
# 12366                                 NaN  UNKNOWN  ...  935a9b9d56d1d0ab26ba4493b64851429510d4e3  def test_line_insert_end(self, name):\n       ...
# 4943                                  NaN  UNKNOWN  ...  b8d0dc73c762bedc0a36bb380cded62a7b3ea162  def test_view_with_bad_login(self):\n        "...
# 
# [10 rows x 10 columns]
print("\nTESTING SAMPLES:")
print(test.sample(10, random_state=SEED))
# TESTING SAMPLES:
#                            __source_file  cve_ids  ...                                       sha                                      function_code
# 2395   functions_for_django_with_cwe.csv  UNKNOWN  ...  25c15b17a86fa95b5374b9ef6366450b28a28b7a  def queryset_add(self, request):\n        """\...
# 1273     functions_for_w3af_with_cwe.csv  UNKNOWN  ...  b48bb3ebb41a074f70805cba57bb518768fe7dfb  def _generate_urls(self, url):\n        '''\n ...
# 1601                                 NaN  UNKNOWN  ...  efe163a1fddfd66fa402231906e96733efddf8af  def test_runs_respected_after_clear(self):\n  ...
# 2651                                 NaN  UNKNOWN  ...  b9224ee28f8d1fe669ae9c09738257bcaf0efd19  def test_default_run_context_tags(patch_script...
# 536   functions_for_airflow_with_cwe.csv  UNKNOWN  ...  cb295c351a016c0a10cab07f2a628b865cff3ca3  def execute(self, context: Context) -> Any:\n ...
# 1671  functions_for_ansible_with_cwe.csv  UNKNOWN  ...  7e3916b767e1f02fae67630ce7e81bdf47825282  def get_capabilities(self):\n        """Return...
# 1099   functions_for_sqlmap_with_cwe.csv  UNKNOWN  ...  84ba3d45c1c129a81f6f784b2b04d0d321423ccf  def getChar(idx, charTbl=None, continuousOrder...
# 1737                                 NaN  UNKNOWN  ...  8eec2d93b6e93b8a1107fb3de2acd68d6994d6ec  def render(self, name, value, attrs=None):\n  ...
# 3125                                 NaN  UNKNOWN  ...  66b02cbec463a7179ab6ac2860dd64553afb74d8  def test_add_spans():\n    trace_manager = InM...
# 1567                                 NaN  UNKNOWN  ...  936e7c4755e503cc2a067398e39d485fc8f0984e  def test_handle_failure_no_task(self, Stats_in...
# 
# [10 rows x 10 columns]
print("\nTRAIN UNIQUE VALUES:")
print(train.nunique())
# TRAIN UNIQUE VALUES:
# __source_file                    15
# cve_ids                          22
# cwe_ids                           1
# file_path                      5602
# label                             2
# patched_function_source       14035
# predicted_cwe_ids                41
# repo                             15
# sha                           10772
# vulnerable_function_source    14193
# dtype: int64
print("\nTEST UNIQUE VALUES:")
print(test.nunique())
# TEST UNIQUE VALUES:
# __source_file                15
# cve_ids                      15
# cwe_ids                       1
# file_path                  2225
# class                         2
# patched_function_source    3538
# predicted_cwe_ids            32
# repo                         15
# sha                        3121
# function_code              3563
# dtype: int64
## }}}

## {{{ unique values in dataset
for name, df, target in [
  ("train", train, "label"),
  ("test", test, "class"),
]:
  print(f"\n{name.upper()} DATASET:")
  print("\nClass Distribution:")
  print(df[target].value_counts(normalize=True))
  for column in [
    "__source_file",
    "cve_ids",
    "cwe_ids",
    "file_path",
    "predicted_cwe_ids",
    "repo",
    "sha",
  ]:
    print("\n")
    print(df[column].value_counts())

  print("\n" + "=" * 60)
# TRAIN DATASET:
# 
# Class Distribution:
# label
# 0    0.557973
# 1    0.442027
# Name: proportion, dtype: float64
# 
# 
# __source_file
# functions_for_sqlmap_with_cwe.csv        841
# functions_for_airflow_with_cwe.csv       837
# functions_for_django_with_cwe.csv        832
# functions_for_salt_with_cwe.csv          826
# functions_for_ansible_with_cwe.csv       821
# functions_for_mlflow_with_cwe.csv        813
# functions_for_w3af_with_cwe.csv          719
# functions_for_tornado_with_cwe.csv       512
# functions_for_jupyter_with_cwe.csv       398
# functions_for_bandit_with_cwe.csv        351
# functions_for_volatility_with_cwe.csv    272
# functions_for_paramiko_with_cwe.csv      272
# functions_for_flask_with_cwe.csv         270
# functions_for_requests_with_cwe.csv      141
# functions_for_yaml_with_cwe.csv           45
# Name: count, dtype: int64
# 
# 
# cve_ids
# UNKNOWN           14218
# CVE-2021-20191        3
# CVE-2018-16859        3
# CVE-2024-24680        2
# CVE-2022-34265        2
# CVE-2022-28346        2
# CVE-2020-11652        2
# CVE-2019-6975         2
# CVE-2020-14343        1
# CVE-2024-39330        1
# CVE-2019-14233        1
# CVE-2019-10906        1
# CVE-2021-25281        1
# CVE-2020-24584        1
# CVE-2016-2512         1
# CVE-2021-45115        1
# CVE-2021-44420        1
# CVE-2020-22935        1
# CVE-2024-39329        1
# CVE-2022-23833        1
# CVE-2024-53908        1
# CVE-2022-22936        1
# Name: count, dtype: int64
# 
# 
# cwe_ids
# UNKNOWN    14248
# Name: count, dtype: int64
# 
# 
# file_path
# lib/core/common.py                                 75
# lib/core/agent.py                                  57
# tornado/web.py                                     56
# lib/request/connect.py                             55
# tests/jobs/test_scheduler_job.py                   55
#                                                    ..
# examples/multistep_workflow/train_keras.py          1
# packaging/release.py                                1
# providers/tests/opsgenie/hooks/test_opsgenie.py     1
# airflow/operators/sensors.py                        1
# salt/modules/smbios.py                              1
# Name: count, Length: 5602, dtype: int64
# 
# 
# predicted_cwe_ids
# CWE-703                      3903
# CWE-Unknown                  2181
# CWE-259                       447
# CWE-89                        438
# UNKNOWN                       351
# CWE-79                        277
# CWE-330                       182
# CWE-327                       167
# CWE-605                       151
# CWE-78                        134
# CWE-94                        101
# CWE-20                         88
# CWE-22                         78
# CWE-259, CWE-703               66
# CWE-502                        65
# CWE-94, CWE-330                38
# CWE-295                        22
# CWE-22, CWE-78                 17
# CWE-327, CWE-330               17
# CWE-89, CWE-703                17
# CWE-78, CWE-703                15
# CWE-94, CWE-703                15
# CWE-330, CWE-703               12
# CWE-605, CWE-703                8
# CWE-327, CWE-703                7
# CWE-327, CWE-330, CWE-703       4
# CWE-732                         3
# CWE-94, CWE-327                 3
# CWE-20, CWE-78                  3
# CWE-89, CWE-502                 3
# CWE-89, CWE-259, CWE-703        2
# CWE-89, CWE-259                 2
# CWE-259, CWE-605                2
# CWE-22, CWE-703                 2
# CWE-78, CWE-327, CWE-330        2
# CWE-502, CWE-703                2
# CWE-259, CWE-327                1
# CWE-20, CWE-703                 1
# CWE-20, CWE-78, CWE-327         1
# CWE-295, CWE-327                1
# CWE-330, CWE-502, CWE-703       1
# Name: count, dtype: int64
# 
# 
# repo
# apache/airflow                     2659
# saltstack/salt                     2480
# django/django                      1857
# mlflow/mlflow                      1600
# ansible/ansible                    1307
# sqlmapproject/sqlmap               1066
# andresriancho/w3af                  719
# tornadoweb/tornado                  579
# jupyter/notebook                    431
# pallets/flask                       376
# PyCQA/bandit                        351
# paramiko/paramiko                   303
# volatilityfoundation/volatility     275
# psf/requests                        195
# yaml/pyyaml                          50
# Name: count, dtype: int64
# 
# 
# sha
# 03349014513114f1eaa413a9831b0027e4fbfa67    164
# 8abdd659087504a45cf0d720c018c6ac28b3937f     62
# 9eeeff414d119c7df72b10da3dda8daf000d85ea     55
# cb295c351a016c0a10cab07f2a628b865cff3ca3     42
# df4293473d2fb6e887e31522cab5aff95e201581     40
#                                            ...
# ea55c15367536a5698b40936a9874a51a76e170a      1
# 477ffd848a9dd4326c66cb33907a2d3e010683ed      1
# ef68fd7ee91ffb156a64d06a819206747550a8a2      1
# bda01cf9939e3069837196c6b4e20314ac877d53      1
# a73eb0592c1a0893687b2313976df2d858484cf4      1
# Name: count, Length: 10772, dtype: int64
# 
# ============================================================
# 
# TEST DATASET:
# 
# Class Distribution:
# class
# 0    0.55066
# 1    0.44934
# Name: proportion, dtype: float64
# 
# 
# __source_file
# functions_for_salt_with_cwe.csv          210
# functions_for_django_with_cwe.csv        209
# functions_for_ansible_with_cwe.csv       206
# functions_for_sqlmap_with_cwe.csv        201
# functions_for_mlflow_with_cwe.csv        199
# functions_for_airflow_with_cwe.csv       194
# functions_for_w3af_with_cwe.csv          157
# functions_for_jupyter_with_cwe.csv       121
# functions_for_tornado_with_cwe.csv       111
# functions_for_bandit_with_cwe.csv         89
# functions_for_volatility_with_cwe.csv     89
# functions_for_flask_with_cwe.csv          71
# functions_for_paramiko_with_cwe.csv       64
# functions_for_requests_with_cwe.csv       28
# functions_for_yaml_with_cwe.csv           13
# Name: count, dtype: int64
# 
# 
# cve_ids
# UNKNOWN           3547
# CVE-2020-11652       2
# CVE-2019-6975        2
# CVE-2022-22936       1
# CVE-2024-41989       1
# CVE-2021-45116       1
# CVE-2019-14232       1
# CVE-2018-16859       1
# CVE-2021-25282       1
# CVE-2019-14234       1
# CVE-2024-45230       1
# CVE-2017-12794       1
# CVE-2022-34265       1
# CVE-2021-20191       1
# CVE-2024-37088       1
# Name: count, dtype: int64
# 
# 
# cwe_ids
# UNKNOWN    3563
# Name: count, dtype: int64
# 
# 
# file_path
# lib/core/common.py                                      20
# tests/admin_views/tests.py                              18
# salt/states/archive.py                                  18
# tests/test_requests.py                                  17
# lib/request/connect.py                                  14
#                                                         ..
# lib/ansible/module_utils/network/vyos/facts/facts.py     1
# lib/ansible/modules/system/filesystem.py                 1
# test/units/parsing/test_ajson.py                         1
# salt/modules/ssh.py                                      1
# tests/pytests/unit/client/ssh/test_ssh.py                1
# Name: count, Length: 2225, dtype: int64
# 
# 
# predicted_cwe_ids
# CWE-703                    1008
# CWE-Unknown                 514
# CWE-259                     114
# CWE-89                      101
# UNKNOWN                      89
# CWE-79                       66
# CWE-330                      55
# CWE-327                      42
# CWE-605                      40
# CWE-78                       32
# CWE-94                       25
# CWE-22                       23
# CWE-20                       21
# CWE-259, CWE-703             16
# CWE-502                      12
# CWE-94, CWE-703               6
# CWE-605, CWE-703              5
# CWE-89, CWE-703               4
# CWE-22, CWE-78                4
# CWE-295                       4
# CWE-94, CWE-330               4
# CWE-330, CWE-703              3
# CWE-94, CWE-327               3
# CWE-89, CWE-502               2
# CWE-502, CWE-703              2
# CWE-327, CWE-330              2
# CWE-78, CWE-703               2
# CWE-20, CWE-78, CWE-327       1
# CWE-22, CWE-703               1
# CWE-20, CWE-703               1
# CWE-259, CWE-605              1
# CWE-20, CWE-605               1
# Name: count, dtype: int64
# 
# 
# repo
# apache/airflow                     680
# saltstack/salt                     600
# django/django                      490
# mlflow/mlflow                      379
# ansible/ansible                    340
# sqlmapproject/sqlmap               249
# andresriancho/w3af                 157
# jupyter/notebook                   129
# tornadoweb/tornado                 126
# pallets/flask                       99
# PyCQA/bandit                        89
# volatilityfoundation/volatility     89
# paramiko/paramiko                   71
# psf/requests                        51
# yaml/pyyaml                         14
# Name: count, dtype: int64
# 
# 
# sha
# 03349014513114f1eaa413a9831b0027e4fbfa67    39
# 8abdd659087504a45cf0d720c018c6ac28b3937f    22
# cb295c351a016c0a10cab07f2a628b865cff3ca3    13
# 9043d9dd05a3b9470abeacd9510752999a7479ae    13
# df4293473d2fb6e887e31522cab5aff95e201581    12
#                                             ..
# 3c75808c5c36a7529a93ac1bba9014907fa3e349     1
# 7eb5f532946686c7173c0d95946aa4b49c010cf1     1
# ebce47de7c72a48b7fbd0a67f0b87b906a8801c1     1
# df7338809bb4246ef028258658d049bedaaaca86     1
# cf57e487e263cc4c47f5eaf39916cb5434d720e8     1
# Name: count, Length: 3121, dtype: int64
# 
# ============================================================
## }}}

## {{{ code length
train_vul_length = train["vulnerable_function_source"].dropna().str.len()
train_patch_length = train["patched_function_source"].dropna().str.len()
print(f"\nTRAIN VULNERABLE CODE:\n{train_vul_length}")
print("\nTRAIN VULNERABLE DESCRIBE:\n", train_vul_length.describe())
print(f"\nTRAIN PATCHED CODE:\n{train_patch_length}")
print("\nTRAIN PATCHED DESCRIBE:\n", train_patch_length.describe())
print("\n" + "=" * 60)
test_vul_length = test["function_code"].dropna().str.len()
test_patch_length = test["patched_function_source"].dropna().str.len()
print(f"\nTEST VULNERABLE CODE:\n{test_vul_length}")
print("\nTEST VULNERABLE DESCRIBE:\n", test_vul_length.describe())
print(f"\nTEST PATCHED CODE:\n{test_patch_length}")
print("\nTEST PATCHED DESCRIBE:\n", test_patch_length.describe())
# TRAIN VULNERABLE CODE:
# 0         226
# 1         490
# 2        5555
# 3         734
# 4        2659
#          ...
# 14243    1703
# 14244     195
# 14245    1013
# 14246     978
# 14247     514
# Name: vulnerable_function_source, Length: 14193, dtype: int64
# 
# TRAIN VULNERABLE DESCRIBE:
#  count    14193.000000
# mean      2473.966251
# std       4420.231884
# min         31.000000
# 25%        560.000000
# 50%       1134.000000
# 75%       2415.000000
# max      47979.000000
# Name: vulnerable_function_source, dtype: float64
# 
# TRAIN PATCHED CODE:
# 0         226
# 1         487
# 2        5048
# 3         752
# 4        2660
#          ...
# 14243    1623
# 14244     195
# 14245    1066
# 14246     919
# 14247     482
# Name: patched_function_source, Length: 14147, dtype: int64
# 
# TRAIN PATCHED DESCRIBE:
#  count    14147.000000
# mean      2519.178554
# std       4429.278376
# min         31.000000
# 25%        582.000000
# 50%       1173.000000
# 75%       2496.500000
# max      47984.000000
# Name: patched_function_source, dtype: float64
# 
# ============================================================
# 
# TEST VULNERABLE CODE:
# 0       1216
# 1        293
# 2        621
# 3       7300
# 4       2163
#         ...
# 3558     286
# 3559    1377
# 3560    1628
# 3561    1067
# 3562    2633
# Name: function_code, Length: 3563, dtype: int64
# 
# TEST VULNERABLE DESCRIBE:
#  count      3563.000000
# mean       2667.377210
# std        6153.767939
# min          32.000000
# 25%         555.000000
# 50%        1126.000000
# 75%        2404.500000
# max      137703.000000
# Name: function_code, dtype: float64
# 
# TEST PATCHED CODE:
# 0        1341
# 1         280
# 2         686
# 3       11407
# 4        2175
#         ...
# 3558      435
# 3559     2019
# 3560     2914
# 3561     1164
# 3562     2639
# Name: patched_function_source, Length: 3545, dtype: int64
# 
# TEST PATCHED DESCRIBE:
#  count      3545.000000
# mean       2713.739633
# std        6179.280056
# min          32.000000
# 25%         580.000000
# 50%        1167.000000
# 75%        2481.000000
# max      137707.000000
# Name: patched_function_source, dtype: float64
#
# train histogram
fig, ax = plt.subplots()
ax.hist(train_vul_length, bins=50, alpha=0.5, color="blue", label="vulnerable")
ax.hist(train_patch_length, bins=50, alpha=0.5, color="red", label="patched")
ax.legend()
ax.set_yscale("log")
ax.set_title("Training Histogram")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "train_histogram.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/train_histogram.png
# train box plot
fig, ax = plt.subplots()
ax.boxplot(
  [train_vul_length, train_patch_length],
  tick_labels=["vulnerable", "patched"], notch=True)
ax.set_ylabel("Code Size")
ax.set_yscale("log")
ax.set_title("Training Box Plot")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "train_boxplot.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/train_boxplot.png
# test histogram
fig, ax = plt.subplots()
ax.hist(test_vul_length, bins=50, alpha=0.5, color="blue", label="vulnerable")
ax.hist(test_patch_length, bins=50, alpha=0.5, color="red", label="patched")
ax.legend()
ax.set_yscale("log")
ax.set_title("Testing Histogram")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "test_histogram.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/test_histogram.png
# test box plot
fig, ax = plt.subplots()
ax.boxplot(
  [test_vul_length, test_patch_length],
  tick_labels=["vulnerable", "patched"], notch=True)
ax.set_ylabel("Code Size")
ax.set_yscale("log")
ax.set_title("Testing Box Plot")
fig.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "test_boxplot.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/test_boxplot.png
# train vulnerable vs patch
train["vulnerable_length"] = train_vul_length
train["patched_length"] = train_patch_length
print("\nTrain Vulnerable vs Patched Length:")
print(train[["vulnerable_length", "patched_length"]].corr())
# Train Vulnerable vs Patched Length:
#                    vulnerable_length  patched_length
# vulnerable_length           1.000000        0.998436
# patched_length              0.998436        1.000000
# training code length visualization
plt.scatter(train["vulnerable_length"], train["patched_length"], alpha=0.3)
plt.xlabel("Vulnerable")
plt.ylabel("Patched")
plt.title("Train Code Length")
plt.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "train_vul_patch_code_length.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/train_vul_patch_code_length.png
# test vulnerable vs patch
test["vulnerable_length"] = test_vul_length
test["patched_length"] = test_patch_length
print("\nTest Vulnerable vs Patched Length:")
print(test[["vulnerable_length", "patched_length"]].corr())
# Test Vulnerable vs Patched Length:
#                    vulnerable_length  patched_length
# vulnerable_length           1.000000        0.999561
# patched_length              0.999561        1.000000
plt.scatter(test["vulnerable_length"], test["patched_length"], alpha=0.3)
plt.xlabel("Vulnerable")
plt.ylabel("Patched")
plt.title("Test Code Length")
plt.savefig(
  os.path.join(
    os.path.abspath(".."),
    "images",
    "test_vul_patch_code_length.png"),
  dpi=300, bbox_inches="tight")
plt.show()
# image saved at ../images/test_vul_patch_code_length.png
## }}}

## {{{ relationship among columns
for name, df, target in [
  ("train", train, "label"),
  ("test", test, "class"),
]:
  print(f"\n{name.upper()} DATASET:")
  print(f"\nREPOSITORIES PER {target.upper()}:")
  print(df.groupby("repo")[target].agg(["count", "sum", "mean"]))
  print("\n", pd.crosstab(df["repo"], df[target], normalize="index"))
  print(f"\nSOURCE FILE PER {target.upper()}:")
  print(pd.crosstab(df["__source_file"], df[target], normalize="index"))
  print("\n", pd.crosstab(df["__source_file"].isna(), df[target], normalize="index"))
  print(f"\nFILE PATH PER {target.upper()}:")
  print(pd.crosstab(df["file_path"], df[target], normalize="index"))
  pattern = r"(?:^|/)(?:test[^/]*|[^/]*test[^/]*)\.py$"
  is_test = df["file_path"].str.contains(
    pattern,
    case=False,
    regex=True,
    na=False,
  )
  print("\n", pd.crosstab(
    is_test,
    df[target],
    normalize="index",
    margins=True,
  ))
  print("\nTesting:\n", df.loc[is_test, ["file_path", target]].sample(10, random_state=SEED))
  print("\nProduction:\n", df.loc[~is_test, ["file_path", target]].sample(10, random_state=SEED))
  print("\n" + "=" * 60)
# 
# TRAIN DATASET:
# 
# REPOSITORIES PER LABEL:
#                                  count   sum      mean
# repo
# PyCQA/bandit                       351     0  0.000000
# andresriancho/w3af                 719     0  0.000000
# ansible/ansible                   1307   486  0.371844
# apache/airflow                    2659  1822  0.685220
# django/django                     1857  1025  0.551966
# jupyter/notebook                   431    33  0.076566
# mlflow/mlflow                     1600   787  0.491875
# pallets/flask                      376   106  0.281915
# paramiko/paramiko                  303    31  0.102310
# psf/requests                       195    54  0.276923
# saltstack/salt                    2480  1654  0.666935
# sqlmapproject/sqlmap              1066   225  0.211069
# tornadoweb/tornado                 579    67  0.115717
# volatilityfoundation/volatility    275     3  0.010909
# yaml/pyyaml                         50     5  0.100000
# 
#  label                                   0         1
# repo
# PyCQA/bandit                     1.000000  0.000000
# andresriancho/w3af               1.000000  0.000000
# ansible/ansible                  0.628156  0.371844
# apache/airflow                   0.314780  0.685220
# django/django                    0.448034  0.551966
# jupyter/notebook                 0.923434  0.076566
# mlflow/mlflow                    0.508125  0.491875
# pallets/flask                    0.718085  0.281915
# paramiko/paramiko                0.897690  0.102310
# psf/requests                     0.723077  0.276923
# saltstack/salt                   0.333065  0.666935
# sqlmapproject/sqlmap             0.788931  0.211069
# tornadoweb/tornado               0.884283  0.115717
# volatilityfoundation/volatility  0.989091  0.010909
# yaml/pyyaml                      0.900000  0.100000
# 
# SOURCE FILE PER LABEL:
# label                                    0
# __source_file
# functions_for_airflow_with_cwe.csv     1.0
# functions_for_ansible_with_cwe.csv     1.0
# functions_for_bandit_with_cwe.csv      1.0
# functions_for_django_with_cwe.csv      1.0
# functions_for_flask_with_cwe.csv       1.0
# functions_for_jupyter_with_cwe.csv     1.0
# functions_for_mlflow_with_cwe.csv      1.0
# functions_for_paramiko_with_cwe.csv    1.0
# functions_for_requests_with_cwe.csv    1.0
# functions_for_salt_with_cwe.csv        1.0
# functions_for_sqlmap_with_cwe.csv      1.0
# functions_for_tornado_with_cwe.csv     1.0
# functions_for_volatility_with_cwe.csv  1.0
# functions_for_w3af_with_cwe.csv        1.0
# functions_for_yaml_with_cwe.csv        1.0
# 
#  label            0    1
# __source_file
# False          1.0  0.0
# True           0.0  1.0
# 
# FILE PATH PER LABEL:
# label                                                 0    1
# file_path
# IPython/frontend/html/notebook/handlers.py          1.0  0.0
# IPython/frontend/html/notebook/kernelmanager.py     1.0  0.0
# IPython/frontend/html/notebook/nbmanager.py         1.0  0.0
# IPython/frontend/html/notebook/notebook.py          1.0  0.0
# IPython/frontend/html/notebook/notebook/handler...  1.0  0.0
# ...                                                 ...  ...
# waf/virusdie.py                                     1.0  0.0
# waf/wallarm.py                                      1.0  0.0
# waf/watchguard.py                                   1.0  0.0
# waf/webknight.py                                    1.0  0.0
# waf/zenedge.py                                      1.0  0.0
# 
# [5602 rows x 2 columns]
# 
#  label             0         1
# file_path
# False      0.722570  0.277430
# True       0.279917  0.720083
# All        0.557973  0.442027
# 
# Testing:
#                                                 file_path  label
# 1760   airflow-core/tests/unit/api_fastapi/common/db/...      1
# 1138                         tornado/test/ioloop_test.py      0
# 2139                     tests/model_fields/test_uuid.py      0
# 12079         django/contrib/gis/gdal/tests/test_geom.py      0
# 2995   w3af/core/controllers/chrome/tests/test_instru...      0
# 2753               tests/tracking/test_model_registry.py      1
# 8614      tests/forms_tests/tests/test_error_messages.py      1
# 4656   tests/store/artifact/test_databricks_artifact_...      1
# 86                                     tests/test_cli.py      1
# 5211                       chart/tests/test_pgbouncer.py      1
# 
# Production:
#                                                 file_path  label
# 8839                                    flask/helpers.py      0
# 12448                         volatility/win32/rawreg.py      0
# 2725                                  bandit/cli/main.py      0
# 7237              w3af/core/data/context/context/html.py      0
# 9756              notebook/services/sessions/handlers.py      0
# 2949                                django/utils/html.py      1
# 5373                            notebook/nbextensions.py      1
# 726                 lib/ansible/plugins/strategy/free.py      0
# 7797   airflow/contrib/operators/gcp_bigtable_operato...      0
# 1461              airflow/utils/log/file_task_handler.py      0
# 
# ============================================================
# 
# TEST DATASET:
# 
# REPOSITORIES PER CLASS:
#                                  count  sum      mean
# repo
# PyCQA/bandit                        89    0  0.000000
# andresriancho/w3af                 157    0  0.000000
# ansible/ansible                    340  134  0.394118
# apache/airflow                     680  486  0.714706
# django/django                      490  281  0.573469
# jupyter/notebook                   129    8  0.062016
# mlflow/mlflow                      379  180  0.474934
# pallets/flask                       99   28  0.282828
# paramiko/paramiko                   71    7  0.098592
# psf/requests                        51   23  0.450980
# saltstack/salt                     600  390  0.650000
# sqlmapproject/sqlmap               249   48  0.192771
# tornadoweb/tornado                 126   15  0.119048
# volatilityfoundation/volatility     89    0  0.000000
# yaml/pyyaml                         14    1  0.071429
# 
#  class                                   0         1
# repo
# PyCQA/bandit                     1.000000  0.000000
# andresriancho/w3af               1.000000  0.000000
# ansible/ansible                  0.605882  0.394118
# apache/airflow                   0.285294  0.714706
# django/django                    0.426531  0.573469
# jupyter/notebook                 0.937984  0.062016
# mlflow/mlflow                    0.525066  0.474934
# pallets/flask                    0.717172  0.282828
# paramiko/paramiko                0.901408  0.098592
# psf/requests                     0.549020  0.450980
# saltstack/salt                   0.350000  0.650000
# sqlmapproject/sqlmap             0.807229  0.192771
# tornadoweb/tornado               0.880952  0.119048
# volatilityfoundation/volatility  1.000000  0.000000
# yaml/pyyaml                      0.928571  0.071429
# 
# SOURCE FILE PER CLASS:
# class                                    0
# __source_file
# functions_for_airflow_with_cwe.csv     1.0
# functions_for_ansible_with_cwe.csv     1.0
# functions_for_bandit_with_cwe.csv      1.0
# functions_for_django_with_cwe.csv      1.0
# functions_for_flask_with_cwe.csv       1.0
# functions_for_jupyter_with_cwe.csv     1.0
# functions_for_mlflow_with_cwe.csv      1.0
# functions_for_paramiko_with_cwe.csv    1.0
# functions_for_requests_with_cwe.csv    1.0
# functions_for_salt_with_cwe.csv        1.0
# functions_for_sqlmap_with_cwe.csv      1.0
# functions_for_tornado_with_cwe.csv     1.0
# functions_for_volatility_with_cwe.csv  1.0
# functions_for_w3af_with_cwe.csv        1.0
# functions_for_yaml_with_cwe.csv        1.0
# 
#  class            0    1
# __source_file
# False          1.0  0.0
# True           0.0  1.0
# 
# FILE PATH PER CLASS:
# class                                              0    1
# file_path
# IPython/frontend/html/notebook/filenbmanager.py  1.0  0.0
# IPython/frontend/html/notebook/handlers.py       1.0  0.0
# IPython/html/allow76.py                          1.0  0.0
# IPython/html/base/handlers.py                    1.0  0.0
# IPython/html/base/zmqhandlers.py                 1.0  0.0
# ...                                              ...  ...
# waf/siteguard.py                                 1.0  0.0
# waf/sonicwall.py                                 1.0  0.0
# waf/urlmaster.py                                 1.0  0.0
# waf/webknight.py                                 1.0  0.0
# waf/wordfence.py                                 1.0  0.0
# 
# [2225 rows x 2 columns]
# 
#  class             0         1
# file_path
# False      0.714350  0.285650
# True       0.279104  0.720896
# All        0.550660  0.449340
# 
# Testing:
#                                                file_path  class
# 1995  tests/api_fastapi/core_api/routes/public/test_...      1
# 1713           tests/ti_deps/deps/test_dagrun_id_dep.py      0
# 1669               test/units/playbook/test_taggable.py      0
# 2210  test/units/modules/network/f5/test_bigip_gtm_p...      1
# 3391                   tests/tracking/test_log_image.py      1
# 2314  airflow-core/tests/unit/api_fastapi/core_api/r...      1
# 1300  tests/providers/amazon/aws/operators/test_glue.py      1
# 1986    tests/cli/commands/test_internal_api_command.py      1
# 3486         tests/regressiontests/admin_views/tests.py      1
# 3546                 tests/unit/templates/jinja_test.py      1
# 
# Production:
#                                         file_path  class
# 1994             lib/ansible/playbook/helpers.py      1
# 495   lib/ansible/executor/task_queue_manager.py      0
# 1202                        tornado/websocket.py      0
# 1882                     lib/ansible/cli/pull.py      1
# 576                       salt/states/archive.py      1
# 3130       lib/ansible/modules/system/systemd.py      0
# 317                    flask/testsuite/appctx.py      0
# 1627                          bandit/cli/main.py      0
# 452      lib/ansible/modules/system/firewalld.py      0
# 823                    plugins/generic/search.py      0
# 
# ============================================================
# 
## }}}

## {{{ inspecting source code
print("\nTRAINING DATASET:")
same = train["vulnerable_function_source"] == train["patched_function_source"]
print(f"same: {train.loc[same, "label"].mean().round(3)}")
print("\n" + "=" * 60)
print("\nTESTING DATASET:")
same = test["function_code"] == test["patched_function_source"]
print(f"same: {test.loc[same, "class"].mean().round(3)}")
# TRAINING DATASET:
# same: 0.457
# 
# ============================================================
# 
# TESTING DATASET:
# same: 0.471

## }}}

## {{{ processing dataset
h1 = train[[
  "repo",
  "vulnerable_function_source",
  "patched_function_source",
  "label"
]]
h1.columns = ["repo", "source_code", "patch", "is_vulnerable"]

h2 = test[[
  "repo",
  "function_code",
  "patched_function_source",
  "class"
]]
h2.columns = ["repo", "source_code", "patch", "is_vulnerable"]

df = pd.concat([h1, h2], ignore_index=True)
df = df.sample(frac=1, random_state=SEED).reset_index(drop=True)
print(df.sample(10, random_state=SEED))
#                        repo                                        source_code                                              patch  is_vulnerable
# 10831       ansible/ansible  def test_update_interval_larger_than_existing_...  def test_update_interval_larger_than_existing_...              1
# 12610        apache/airflow  def test_cli_assets_materialize(parser: Argume...  def test_cli_assets_materialize(parser: Argume...              1
# 14713        saltstack/salt  def _run(cmd,\n         cwd=None,\n         st...  def _run(cmd,\n         cwd=None,\n         st...              1
# 9520         apache/airflow  def get_conn(self):\n        conn = self.get_c...  def get_conn(self):\n        conn = self.get_c...              0
# 1201   sqlmapproject/sqlmap  def getFingerprint(self):\n        value = ""\...  def getFingerprint(self):\n        value = ""\...              0
# 1137     tornadoweb/tornado  def _value_from_stopiteration(e):\n    try:\n ...  def _value_from_stopiteration(e):\n    try:\n ...              0
# 16152        apache/airflow  def test_parms_not_passed_is_empty_dict(self):...  def test_parms_not_passed_is_empty_dict(self):...              1
# 15519         django/django  def get_backend_timeout(self, timeout=DEFAULT_...  def get_backend_timeout(self, timeout=DEFAULT_...              0
# 14600         django/django  def test_chunked(self):\n        "The static v...  def test_chunked(self):\n        "The static v...              0
# 3779        ansible/ansible  def __init__(self):\n\n        super(CallbackM...  def __init__(self):\n\n        super(CallbackM...              0
print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 17811 entries, 0 to 17810
# Data columns (total 4 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   repo           17811 non-null  str
#  1   source_code    17756 non-null  str
#  2   patch          17692 non-null  str
#  3   is_vulnerable  17811 non-null  int64
# dtypes: int64(1), str(3)
# memory usage: 556.7 KB
# None
#
# ast parsable check
import ast

def can_parse(source):
  try:
    ast.parse(source)
    return True
  except (SyntaxError, NameError, ValueError, TypeError):
    return False

source_code = df["source_code"].apply(can_parse)
patched_code = df["patch"].apply(can_parse)
print(f"Parsable source code: {source_code.sum()}")
print(f"Parsable patched code: {patched_code.sum()}")
# Parsable source code: 17756
# Parsable patched code: 17692
df = df[(source_code & patched_code)]
print(df.info())
# <class 'pandas.DataFrame'>
# Index: 17692 entries, 0 to 17809
# Data columns (total 4 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   repo           17692 non-null  str
#  1   source_code    17692 non-null  str
#  2   patch          17692 non-null  str
#  3   is_vulnerable  17692 non-null  int64
# dtypes: int64(1), str(3)
# memory usage: 691.1 KB
# None
#
# saving dataset
filename = os.path.join(os.path.abspath(".."), "data", "processed", "dataset.csv")
df.to_csv(filename, index=False)
print(f"dataset saved at {filename}")
## }}}


