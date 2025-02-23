package com.spring_playground.spring_playground.ioc;

import org.springframework.stereotype.Component;

@Component
public class IoCBean {
	public String hello() {
        return "Hello!";
    }
}
