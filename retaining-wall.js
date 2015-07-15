function sum(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

/**
 * retaining wall problem,
 * given woodLengths an array of sizes of wood you have, and requiredLengths
 */
var retainingWall = (function ($) {
    "use strict";
    var self = {};

    self.solveRecursive = function (woodLengths, requiredLengths) {
        if (requiredLengths.length <= 0) {
            return sum(woodLengths)
        }
        var noCuts = true;
        for (var i = 0; i < woodLengths.length; i++) {
            var woodLength = woodLengths[i];
            //return min of all cuts


        }
        if (noCuts) {
            return false;
        }
    };
    self.solve = function (woodLengths, requiredLengths) {
        return self.solveRecursive(woodLengths, requiredLengths, )
    };
    return self;
})(jQuery);
