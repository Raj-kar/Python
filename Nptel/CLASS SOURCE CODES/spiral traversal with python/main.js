function matrix(n) {
    const result = []

    for (i = 0; i < n; i++) {
        result.push([])
    }

    let counter = 1
    let startRow = 0
    let startColumn = 0
    let endRow = n - 1
    let endColumn = n - 1

    while (startRow <= endRow && startColumn <= endColumn) {
        for (let i = startColumn; i <= endColumn; i++) {
            result[startRow][i] = counter
            counter++
        }
        startRow++

        for (let i = startRow; i <= endRow; i++) {
            result[i][endColumn] = counter
            counter++
        }
        endColumn--

        for (let i = endColumn; i >= startColumn; i--) {
            result[endRow][i] = counter
            counter++
        }
        endRow--

        for (let i = endRow; i >= startRow; i--) {
            result[i][startColumn] = counter
            counter++
        }
        startColumn++
    }

    return result
}

console.log(matrix(5))