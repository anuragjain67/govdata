angular.module('pincodeApp', []);

angular.module('pincodeApp')

.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
}])

.service('Pincode', ['$http', function($http){
  return {
    getPincodes : function(q) {
      return $http({
        method: 'GET',
        url: '/api/pincodes/',
        params: {
          'q': q
        }
        });
    }
  }
}])

.controller('searchPincodeCtrl', ['$scope', 'Pincode', function($scope, Pincode) {
  $scope.pincodes = [];
  $scope.numberOfResults = null;
  $scope.getPincodes = function () {
    var httpRequest = Pincode.getPincodes($scope.searchTerm);
    httpRequest.success(function(data, status, headers, config){
      $scope.pincodes = data.objects;
      $scope.numberOfResults = data.meta.total_count;
    })
  }
}]);
