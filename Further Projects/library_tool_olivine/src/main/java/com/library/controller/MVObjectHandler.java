package com.library.controller;

import org.springframework.web.servlet.ModelAndView;

import static com.library.securityUtil.SecurityUtil.returnRole;

public class MVObjectHandler {

    private static String[][] adminLinks = {
        {"/admin/users", "reg usersButton", "users"},
        {"/common/books", "reg booksButton", "books"},
        {"/common/borrowings", "reg borrowingsButton", "borrowings"}
    };

    private static String[][] userLinks = {
        {"/common/books", "reg booksButton", "books"},
        {"/common/borrowings", "reg borrowingsButton", "borrowings"}
    };

    public static void addToEachModelAndView(ModelAndView modelAndView) {
        boolean adminOrNot = returnRole().contains("admin");
        modelAndView.addObject("auth", adminOrNot);
        modelAndView.addObject("links", adminOrNot ? adminLinks : userLinks);
    }



}
