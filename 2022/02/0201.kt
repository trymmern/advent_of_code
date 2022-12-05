import java.io.File

val x = mapOf("B" to 0, "A" to 3, "C" to 6)
val y = mapOf("C" to 0, "B" to 3, "A" to 6)
val z = mapOf("A" to 0, "C" to 3, "B" to 6)
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
                return score + 1
            }
        }
        "Y" -> {
            var score = y[match[0]]
            if (score != null) {
                return score + 2
            }
        }
        "Z" -> {
            var score = z[match[0]]
            if (score != null) {
                return score + 3
            }
        }
        else -> {
            println("wut")
        }
    }
    return -1
}