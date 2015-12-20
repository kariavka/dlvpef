app.controller("FeedbackCtrl", ["$scope", function($scope) {
'use strict';
    // Form fields.
    $scope.full_name = new CharField({min_length:3, required:true});
    $scope.category = new CharField({min_length:3, required:true});
    $scope.subject = new CharField({min_length:3, required:true});
    $scope.message = new CharField({min_length:3, required:true});

    $scope.formIsNotValid = function() {
        // Returns ``True`` if the form is filled out incorrectly.
        var result = false,
            fields = [$scope.full_name, $scope.category, $scope.subject,
            $scope.message];

        for (var i=0; i<fields.length; ++i) {
            var field = fields[i];
            if (!field.isClean() || !field.model) {
                result = true;
                break;
            }
        }

        return result;
    } // end formIsNotValid().

    $('#feedback-form').submit(function() {
        // Prohibit send a bad form data.
        if ($scope.formIsNotValid())
            return false;

        return true;
    }); // end submit().

}]);
