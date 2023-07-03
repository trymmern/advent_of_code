import java.io.File

fun main() {
    var score = 0
    File("input.txt").forEachLine{ it ->
        var x = it.split(",")
        var x1 = x[0].split("-")
        var x2 = x[1].split("-")

        var x1_start = x1[0]
        var x1_end = x1[1]

        var x2_start = x2[0]
        var x2_end = x2[1]

        if ((x2_start <= x1_start && x1_end <= x2_end) || (x1_start <= x2_start && x2_end <= x1_end)) {
            score += 1
        }
    }
    println("Score: " + score)
}

main()