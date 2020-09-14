// Tutorial from https://dzone.com/articles/wordcount-with-spark-and-scala

 val text = sc.textFile("/tmp/word_count.txt");
 val counts = text.flatMap(line => line.split(" ")).map(word => (word,1)).reduceByKey(_+_); 
 counts.collect;

