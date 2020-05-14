################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/main.c \
../src/py_call_super.c \
../src/py_import_call_execute.c 

OBJS += \
./src/main.o \
./src/py_call_super.o \
./src/py_import_call_execute.o 

C_DEPS += \
./src/main.d \
./src/py_call_super.d \
./src/py_import_call_execute.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -std=c11 -I/home/tangc/apps/python-3.8.2/include/python3.8 -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


