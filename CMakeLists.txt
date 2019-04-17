cmake_minimum_required(VERSION 3.13)
project(cppcoro LANGUAGES CXX)

set(CMAKE_CXX_EXTENSIONS OFF)

add_library(cppcoro)
target_sources(cppcoro PRIVATE
	"lib/async_auto_reset_event.cpp"
	"lib/async_manual_reset_event.cpp"
	"lib/async_mutex.cpp"
	"lib/cancellation_state.cpp"
	"lib/cancellation_token.cpp"
	"lib/cancellation_source.cpp"
	"lib/cancellation_registration.cpp"
	"lib/lightweight_manual_reset_event.cpp"
	"lib/ip_address.cpp"
	"lib/ip_endpoint.cpp"
	"lib/ipv4_address.cpp"
	"lib/ipv4_endpoint.cpp"
	"lib/ipv6_address.cpp"
	"lib/ipv6_endpoint.cpp"
	"lib/static_thread_pool.cpp"
	"lib/auto_reset_event.cpp"
	"lib/spin_wait.cpp"
	"lib/spin_mutex.cpp")

if(WIN32)
	target_sources(cppcoro PRIVATE
	    "lib/win32.cpp"
	    "lib/io_service.cpp"
	    "lib/file.cpp"
	    "lib/readable_file.cpp"
	    "lib/writable_file.cpp"
	    "lib/read_only_file.cpp"
	    "lib/write_only_file.cpp"
	    "lib/read_write_file.cpp"
	    "lib/file_read_operation.cpp"
	    "lib/file_write_operation.cpp"
	    "lib/socket_helpers.cpp"
	    "lib/socket.cpp"
	    "lib/socket_accept_operation.cpp"
	    "lib/socket_connect_operation.cpp"
	    "lib/socket_disconnect_operation.cpp"
	    "lib/socket_send_operation.cpp"
	    "lib/socket_send_to_operation.cpp"
	    "lib/socket_recv_operation.cpp"
		"lib/socket_recv_from_operation.cpp")
endif()

target_include_directories(cppcoro PUBLIC 
	$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/include>
	$<INSTALL_INTERFACE:include>)
target_compile_features(cppcoro PUBLIC cxx_std_20)

install(TARGETS cppcoro EXPORT cppcoroTargets
	LIBRARY DESTINATION lib
	ARCHIVE DESTINATION lib
	RUNTIME DESTINATION bin)
install(DIRECTORY include DESTINATION .)

export(EXPORT cppcoroTargets
  FILE "${CMAKE_CURRENT_BINARY_DIR}/cppcoro/cppcoroTargets.cmake"
  NAMESPACE cppcoro::)
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/cppcoro/cppcoroConfig.cmake
	"include(\"\${CMAKE_CURRENT_LIST_DIR}/cppcoroTargets.cmake\")")

set(config_package_location lib/cmake/cppcoro)
install(EXPORT cppcoroTargets
  FILE cppcoroTargets.cmake
  NAMESPACE cppcoro::
  DESTINATION ${config_package_location})
install(
  FILES ${CMAKE_CURRENT_BINARY_DIR}/cppcoro/cppcoroConfig.cmake
  DESTINATION ${config_package_location}
  COMPONENT Devel)
