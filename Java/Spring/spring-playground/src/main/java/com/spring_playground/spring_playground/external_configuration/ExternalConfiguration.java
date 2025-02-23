package com.spring_playground.spring_playground.examples.external_configuration;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class ExternalConfiguration {
    @Value("${app.name}")
    private String applicationName;

    public void printAppName() {
        System.out.println("Application running: " + applicationName);
    }
}

