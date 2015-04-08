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
  $scope.numberOfShownData = null;
  $scope.showPaginationAlert = false;

  // Adding for loading display
  $scope.loader = {};
  $scope.loader.loading = false;


  $scope.getPincodes = function () {
    $scope.loader.loading = true;
    var httpRequest = Pincode.getPincodes($scope.searchTerm);
    httpRequest.success(function(data, status, headers, config){
      $scope.pincodes = data.objects;
      $scope.numberOfResults = data.meta.total_count;
      if (data.meta.next == null){
        $scope.numberOfShownData = data.meta.total_count;
      }
      else{
        $scope.numberOfShownData = data.meta.limit;
        $scope.showPaginationAlert = true;
      }
      $scope.loader.loading = false;
    })
  }
}]);
