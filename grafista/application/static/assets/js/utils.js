function parseSamples(data) {
    var processedArray = [];
    var parsedData = data;
    var samplesArray = parsedData['samples'];
    var arrayLength = samplesArray.length;
    for (var i = 0; i < arrayLength; i++) {
        var date = new Date(samplesArray[i][0]);
        processedArray.push({x: date.getTime(), y: samplesArray[i][1]})
    }
    // console.log(processedArray);
    return processedArray;
}
