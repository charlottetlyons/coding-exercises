package com.spring_playground.spring_playground.external_configuration;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.spring_playground.spring_playground.external_configuration.ExternalConfiguration;

@RestController
public class ExternalConfigurationController {
    
    @Autowired
    private final ExternalConfiguration externalConfiguration;

    public ExternalConfigurationController(ExternalConfiguration ec) {
        this.externalConfiguration = ec;
    }

    @GetMapping("/ext-config")
    public String hello() {
        externalConfiguration.printAppName();
        return "done";
    }
}
