package sample.demo;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class SampleController {
    @GetMapping("/")
    public String getGreetings() {
        return "Hello world Buddy! 🐼🪵🐫🌵";
    }
    @GetMapping("/movies")
    public String getMovies() {
        return "All good nice telugu movies are here 🎥 🦸";
    }
}
