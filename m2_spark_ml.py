# SE446 - Milestone 2
# Spark ML Pipeline Script
#
# Original ML code by : 
#Joud Alhozami (ID:231682)
#
# converted and organized as a standalone script by: Layan Alshammari (ID:231822)
#
#  this file is the standalone Python script used for spark-submit.
# it's based on the ML part of the project, which includes:
# - Task 5: Feature Engineering Pipeline
from pyspark.sql.functions import col, hour, to_timestamp
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier, GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator
import time
from pyspark.sql import SparkSession

#loading the dataset and addingthe spark seesion to work here 
spark = SparkSession.builder \
    .appName("M2_Spark_ML_GroupAlmudaiheem") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

print("Spark Master:", spark.sparkContext.master)
print("Spark Version:", spark.version)

data_path = "hdfs:///data/chicago_crimes.csv"

df = spark.read.csv(
    data_path,
    header=True,
    inferSchema=True
)

print("Original row count:", df.count())

df = df.sample(0.05, seed=42)

print("Sampled row count for ML:", df.count())




# how we loaded it in google colab
#ml_df = df
#ml_df = ml_df.select(
#    "PrimaryType",
#    "Domestic_str",
#    "District",
#    "Hour",
#    "label"
#).dropna()

ml_df = df.withColumn(
    "Hour",
    hour(to_timestamp(col("Date"), "MM/dd/yyyy hh:mm:ss a"))
).withColumn(
    "label",
    col("Arrest").cast("integer")
).select(
    col("Primary Type"),
    col("Domestic").cast("string").alias("Domestic_str"),
    col("District").cast("double"),
    col("Hour").cast("double"),
    col("label")
).dropna()

ml_df.show(5)

crime_indexer = StringIndexer(
    inputCol="Primary Type",
    outputCol="crime_index",
    handleInvalid="skip"
)

domestic_indexer = StringIndexer(
    inputCol="Domestic_str",
    outputCol="domestic_index",
    handleInvalid="skip"
)

assembler = VectorAssembler(
    inputCols=["District", "crime_index", "Hour", "domestic_index"],
    outputCol="features"
)

feature_pipeline = Pipeline(stages=[
    crime_indexer,
    domestic_indexer,
    assembler
])

feature_model = feature_pipeline.fit(ml_df)
prepared_df = feature_model.transform(ml_df)

train_df, test_df = prepared_df.randomSplit([0.8, 0.2], seed=42)

prepared_df.select(
    "District",
    "crime_index",
    "Hour",
    "domestic_index",
    "features",
    "label"
).show(5, truncate=False)

print("Feature vector positions:")
print("[0] District, [1] crime_index, [2] Hour, [3] domestic_index")


# - Task 6: Training and Evaluating Three Models

# Author: Joud Alhozami (ID: 231682)
# Fixed by: Fjr Sad (ID: 231722)


if train_df.count() < 50:
    print("Small training dataset detected. Combining train_df and test_df for local execution stability.")
    combined_df = train_df.unionByName(test_df).cache()
    train_df = combined_df
    test_df = combined_df

models = {
    "Logistic Regression": LogisticRegression(
        featuresCol="features",
        labelCol="label",
        maxIter=100,
        regParam=0.01
    ),

    "Random Forest": RandomForestClassifier(
        featuresCol="features",
        labelCol="label",
        numTrees=100,
        maxDepth=5,
        maxBins=32,
        seed=42
    ),

    "GBT": GBTClassifier(
        featuresCol="features",
        labelCol="label",
        maxIter=50,
        maxDepth=5,
        maxBins=32,
        seed=42
    )
}

auc_eval = BinaryClassificationEvaluator(
    labelCol="label",
    rawPredictionCol="rawPrediction",
    metricName="areaUnderROC"
)

accuracy_eval = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

f1_eval = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="f1"
)

precision_eval = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedPrecision"
)

recall_eval = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedRecall"
)

results = []
trained_models = {}

for name, clf in models.items():
    start_time = time.time()

    model = clf.fit(train_df)
    predictions = model.transform(test_df)

    training_time = time.time() - start_time

    auc = auc_eval.evaluate(predictions)
    accuracy = accuracy_eval.evaluate(predictions)
    f1 = f1_eval.evaluate(predictions)
    precision = precision_eval.evaluate(predictions)
    recall = recall_eval.evaluate(predictions)

    print("=" * 50)
    print("Model:", name)
    print("AUC-ROC:", auc)
    print("Accuracy:", accuracy)
    print("F1 Score:", f1)
    print("Precision:", precision)
    print("Recall:", recall)
    print("Training Time:", training_time)

    print("Confusion Matrix:")
    predictions.groupBy("label", "prediction").count().orderBy("label", "prediction").show()

    results.append((name, auc, accuracy, f1, precision, recall, training_time))
    trained_models[name] = model

results_df = spark.createDataFrame(
    results,
    ["Model", "AUC_ROC", "Accuracy", "F1_Score", "Precision", "Recall", "Training_Time"]
)

print("Model Comparison Table:")
results_df.show(truncate=False)




# - Task 7: Feature Importances and Interpretation

rf_model = trained_models["Random Forest"]

feature_names = ["District", "crime_index", "Hour", "domestic_index"]
importances = rf_model.featureImportances.toArray()

importance_data = [(feature_names[i], float(importances[i])) for i in range(len(feature_names))]

importance_df = spark.createDataFrame(
    importance_data,
    ["Feature", "Importance"]
).orderBy(col("Importance").desc())

importance_df.show(truncate=False)

print("Interpretation:")
print(
    "The most important feature is the one with the highest score. "
    "If crime_index is the highest, it means the crime type matters the most when predicting "
    "if an arrest will happen. Random Forest and GBT can do better than Logistic Regression" \
    " because they can understand more complex patterns."
)


spark.stop()