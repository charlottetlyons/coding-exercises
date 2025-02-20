package com.spring_playground.spring_playground.examples;

import org.springframework.stereotype.Component;

@Component
public class SpringIoCBean {
    public String doThing() {
        return "Thing done!";
    }
}