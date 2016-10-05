package com.library.controller;

import com.library.model.business.Borrowing;
import com.library.requests.book.BookRequests;
import com.library.requests.borrowing.BorrowingRequests;
import com.library.requests.user.UserRequests;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;
import javax.servlet.http.HttpServletRequest;

import java.util.Map;

import static com.library.controller.MVObjectHandler.addToEachModelAndView;
import static com.library.securityUtil.SecurityUtil.returnRole;
import static com.library.securityUtil.SecurityUtil.returnUserName;

@Controller
public class NavigationController {

    @Autowired
    BookRequests bookRequest;

    @Autowired
    UserRequests userRequest;

    @Autowired
    BorrowingRequests borrowingRequest;

    @RequestMapping(value = "common/books", method= RequestMethod.GET)
    public ModelAndView books(HttpServletRequest request) {
        ModelAndView modelAndView = new ModelAndView();

        returnUserName();

        modelAndView.addObject("books", (bookRequest.listAllBooks()).books);
        addToEachModelAndView(modelAndView);
        modelAndView.setViewName("authorized/common/books");
        return modelAndView;
    }

    @RequestMapping(value="/common/books", method= RequestMethod.POST)
    public ModelAndView borrowBook(@RequestParam Map<Integer, Integer> requestParams) {
        Borrowing borrowing = new Borrowing((int)requestParams.get("user_id"), (int)requestParams.get("book_id"));
        borrowingRequest.setNewBorrowing(borrowing);
        ModelAndView modelAndView = new ModelAndView();
        addToEachModelAndView(modelAndView);
        modelAndView.setViewName("authorized/common/books");
        return modelAndView;
    }

    @RequestMapping(value = "admin/users", method= RequestMethod.GET)
    public ModelAndView users() {
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.addObject("users", (userRequest.getAllUsers()).users);
        addToEachModelAndView(modelAndView);
        modelAndView.setViewName("authorized/admin/users");
        return modelAndView;
    }

    @RequestMapping(value = "common/borrowings", method= RequestMethod.GET)
    public ModelAndView adminBorrowings(HttpServletRequest request) {
        ModelAndView modelAndView = new ModelAndView();
        boolean adminOrNot = returnRole().contains("admin");
        modelAndView.addObject("borrowings", adminOrNot ? borrowingRequest.getAllBorrowings().borrowings : borrowingRequest.getUserBorrowings(request.getRemoteUser()).borrowings);
        addToEachModelAndView(modelAndView);
        modelAndView.setViewName("authorized/common/borrowings");
        return modelAndView;
    }


}
