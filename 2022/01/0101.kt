import java.io.File

fun main() {
    var max: Int = 0
    var counter: Int = 0
    var cont: Boolean = false
    
    File("input.txt").forEachLine { it ->
        if (it.isEmpty()) {
            if (counter > max) {
                max = counter
            }
            counter = 0
            cont = true
        }
        if (!cont) {
            counter += it.toInt()
        }
        cont = false
    }
    println(max)
}