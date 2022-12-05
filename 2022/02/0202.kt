import java.io.File

val x = mapOf("B" to 1, "A" to 3, "C" to 2)
val y = mapOf("C" to 3, "B" to 2, "A" to 1)
val z = mapOf("A" to 2, "C" to 1, "B" to 3)
fun main() {

    var score: Int = 0

    File("input.txt").forEachLine { it ->
        var match = it.replace("\n", "").split(" ").toTypedArray()
        score += getScore(match)
    }
    println(score)
}

fun getScore(match: Array<String>): Int {
    when (match[1]) {
        "X" -> {
            var score = x[match[0]]
            if (score != null) {
                return score + 0
            }
        }
        "Y" -> {
            var score = y[match[0]]
            if (score != null) {
                return score + 3
            }
        }
        "Z" -> {
            var score = z[match[0]]
            if (score != null) {
                return score + 6
            }
        }
        else -> {
            println("wut")
        }
    }
    return -1
}